from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
from sqlalchemy import func, or_
from sqlalchemy import not_
import os

app = Flask(__name__, static_url_path='/static')

# --- SECURE DATABASE CONFIGURATION ---
# These pull dynamically from your docker-compose.yml / .env file
db_user = os.environ.get('POSTGRES_USER')
db_pw = os.environ.get('POSTGRES_PW')
db_host = os.environ.get('POSTGRES_HOST')
db_name = os.environ.get('POSTGRES_DB')

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql+psycopg2://{db_user}:{db_pw}@{db_host}/{db_name}'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class BasePlant(db.Model):
    __abstract__ = True

    plant_id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String())
    image_type = db.Column(db.String())
    image_url = db.Column(db.String())
    scientific_name = db.Column(db.String())
    plant_type = db.Column(db.String())
    source = db.Column(db.String())
    location_counties = db.Column(db.String())

    def __init__(self, plant_name: str, image_type: str, image_url: str, scientific_name: str, plant_type: str, source: str, location_counties: str) -> None:
        self.plant_name = plant_name
        self.image_type = image_type
        self.image_url = image_url
        self.scientific_name = scientific_name
        self.plant_type = plant_type
        self.source = source
        self.location_counties = location_counties

class Trees(BasePlant):
    __tablename__ = 'trees'

class Flowers(BasePlant):
    __tablename__ = 'flower'

class Vines(BasePlant):
    __tablename__ = 'vines'   

class Cacti(BasePlant):
    __tablename__ = 'cacti' 

class Grasses(BasePlant):
    __tablename__ = 'grasses' 

class Aquatic(BasePlant):
    __tablename__ = 'aquatic_plants'  

tables = [Trees, Flowers, Vines, Cacti, Grasses, Aquatic]       


def get_valid_image_filters(model_class):
    """
    Returns a list of robust SQLAlchemy filter criteria to ensure the image_url
    is a real, non-empty, and non-placeholder URL or file path.
    """
    return [
        model_class.image_url.is_not(None),
        model_class.image_url != '',
        func.trim(model_class.image_url) != '',
        not_(func.lower(func.trim(model_class.image_url)).in_(['none', 'null', 'nan', 'n/a', 'undefined', 'placeholder'])),
        # Ensure it either starts with a web/static address, or ends with a standard image file extension
        or_(
            func.lower(model_class.image_url).like('http://%'),
            func.lower(model_class.image_url).like('https://%'),
            func.lower(model_class.image_url).like('/static/%'),
            func.lower(model_class.image_url).like('static/%'),
            func.lower(model_class.image_url).like('%.jpg'),
            func.lower(model_class.image_url).like('%.jpeg'),
            func.lower(model_class.image_url).like('%.png'),
            func.lower(model_class.image_url).like('%.webp'),
            func.lower(model_class.image_url).like('%.gif'),
            func.lower(model_class.image_url).like('%.svg')
        )
    ]


def is_valid_local_image(url):
    """
    Checks if an image URL is valid and physically exists if it is a local path on disk.
    This prevents matching images that are defined in the database but missing from your folder.
    """
    if not url:
        return False
    url_str = str(url).strip()
    url_lower = url_str.lower()
    
    # Exclude placeholders and missing representations
    if url_lower in ['', 'none', 'null', 'nan', 'n/a', 'undefined', 'placeholder']:
        return False
        
    # Ensure there's a dot for file extensions/domains
    if '.' not in url_str:
        return False
        
    # If it's an external web image, we assume it's valid (cannot ping external sites synchronously without slowing down loading times)
    if url_lower.startswith('http://') or url_lower.startswith('https://'):
        return True
        
    # If it is a local static path, check if the file physically exists on disk
    if url_lower.startswith('/static/') or url_lower.startswith('static/'):
        # Strip leading slash to look for standard relative paths (e.g. 'static/images/...')
        relative_path = url_str.lstrip('/')
        return os.path.exists(relative_path)
        
    return True
        

@app.route('/')
def render_webpage():
    unique_species = [db.session.query(func.count(func.distinct(func.lower(table.plant_name)))).scalar() for table in tables]

    # Accumulate all plants across all tables that have valid image URLs to show on the landing page
    valid_plants = []
    seen_names = set()

    # Shuffle tables to ensure a fun, dynamic layout on reload
    shuffled_tables = list(tables)
    random.shuffle(shuffled_tables)

    for table in shuffled_tables:
        if table == Trees:
            # For Trees, we avoid showing 'bark' on the home page for general visual consistency
            query_results = table.query.filter(
                not_(table.image_type == 'bark'),
                *get_valid_image_filters(table)
            ).all()
        else:
            query_results = table.query.filter(
                *get_valid_image_filters(table)
            ).all()

        for plant in query_results:
            name_lower = plant.plant_name.lower()
            if name_lower not in seen_names:
                # Double-check physical existence of image files on disk
                if is_valid_local_image(plant.image_url):
                    valid_plants.append(plant)
                    seen_names.add(name_lower)

    # Shuffle the pool of valid image-bearing plants
    random.shuffle(valid_plants)

    # Take the top 4 unique plants with valid images
    plants_for_home = valid_plants[:4]

    # Extreme fallback: if we have fewer than 4 plants with images (unlikely), fill with any plants
    if len(plants_for_home) < 4:
        for table in shuffled_tables:
            if len(plants_for_home) >= 4:
                break
            all_plants = table.query.all()
            random.shuffle(all_plants)
            for plant in all_plants:
                if len(plants_for_home) >= 4:
                    break
                name_lower = plant.plant_name.lower()
                if name_lower not in seen_names:
                    plants_for_home.append(plant)
                    seen_names.add(name_lower)

    # Extract details safely
    plant_names = [item.plant_name if item else "Unknown" for item in plants_for_home]
    plant_image_url = [item.image_url if item else "" for item in plants_for_home]
    scientific_names = [item.scientific_name if item else "" for item in plants_for_home]
    plant_types = [item.plant_type if item else "" for item in plants_for_home]
    source = [item.source if item else "" for item in plants_for_home]

    plant_options = set()

    # Fetch unique plant names from each table that has county data
    for TableClass in tables:
        plants_with_counties = TableClass.query.filter(TableClass.location_counties != '').all()
        for plant in plants_with_counties:
            plant_options.add(plant.plant_name)

    plant_options = sorted(plant_options, key=lambda x: x.split()[0][0].lower())    

    return render_template('index.html', plant_names=plant_names, plant_image_url=plant_image_url, scientific_names=scientific_names, plant_types=plant_types, source=source, unique_species=unique_species, plant_options=plant_options, current_route='render_webpage')

@app.route('/plantInfo/')
def render_plant_info():
    return render_template('plantInfo.html')

@app.route('/cropData')
def render_crop_data():
    return render_template('cropData.html')

@app.route('/get_plant_name_list')
def get_plant_name_list():
    switchState_trees = request.args.get('switchState_trees')
    switchState_leaves = request.args.get('switchState_leaves')
    switchState_barks = request.args.get('switchState_barks')
    switchState_wildflowers = request.args.get('switchState_wildflowers')
    switchState_grasses = request.args.get('switchState_grasses')
    switchState_aquaticplants = request.args.get('switchState_aquaticplants')
    switchState_vines = request.args.get('switchState_vines')
    switchState_cacti = request.args.get('switchState_cacti')
    randomIndex = request.args.get('randomIndex')
    previousPlantName = request.args.get('previousPlantName')

    # Parse target index. If it is undefined, empty, or out of bounds,
    # we generate a random index (0-3) on the backend so it shuffles naturally!
    try:
        target_idx = int(randomIndex)
        if target_idx < 0 or target_idx > 3:
            target_idx = random.randint(0, 3)
    except (TypeError, ValueError):
        target_idx = random.randint(0, 3)

    # Collect active category configurations based on the switch states
    active_categories = []
    if switchState_trees == 'true':
        active_categories.append((Trees, Trees.image_type == 'close_fullsize'))
    if switchState_leaves == 'true':
        active_categories.append((Trees, Trees.image_type == 'leaf'))    
    if switchState_barks == 'true':
        active_categories.append((Trees, Trees.image_type == 'bark'))
    if switchState_wildflowers == 'true':
        active_categories.append((Flowers, None))
    if switchState_vines == 'true':
        active_categories.append((Vines, None))
    if switchState_cacti == 'true':
        active_categories.append((Cacti, None))                
    if switchState_grasses == 'true':
        active_categories.append((Grasses, None))           
    if switchState_aquaticplants == 'true':
        active_categories.append((Aquatic, None))

    # Safely default to Trees if no switches are turned on
    if not active_categories:
        active_categories.append((Trees, Trees.image_type == 'close_fullsize'))

    # 1. FIND THE CORRECT PLANT (Must have a valid image URL)
    correct_plant = None
    prev_name = previousPlantName.strip() if previousPlantName else ""

    # Try active categories first
    categories_shuffled = list(active_categories)
    random.shuffle(categories_shuffled)
    for model_class, extra_filter in categories_shuffled:
        query = model_class.query.filter(
            func.lower(model_class.plant_name) != func.lower(prev_name),
            *get_valid_image_filters(model_class)
        )
        if extra_filter is not None:
            query = query.filter(extra_filter)
        
        # Pull a few candidates to test local file existence in Python!
        candidates = query.order_by(db.func.random()).limit(10).all()
        for candidate in candidates:
            if is_valid_local_image(candidate.image_url):
                correct_plant = candidate
                break
        if correct_plant:
            break

    # Fallback: if no active category has a valid image, pull any random plant with an image
    if not correct_plant:
        for table in tables:
            query = table.query.filter(*get_valid_image_filters(table))
            candidates = query.order_by(db.func.random()).limit(10).all()
            for candidate in candidates:
                if is_valid_local_image(candidate.image_url):
                    correct_plant = candidate
                    break
            if correct_plant:
                break

    # Console debug log to instantly identify what the backend chose and what its URL is!
    if correct_plant:
        print(f"[DEBUG] Chosen correct plant: {correct_plant.plant_name} | Class: {correct_plant.__class__.__name__} | URL: '{correct_plant.image_url}'", flush=True)
    else:
        print("[DEBUG] Warning: No correct plant could be found matching valid image criteria!", flush=True)

    # 2. SELECT 3 UNIQUE DECOY PLANTS (Decoys do not require images, just unique names)
    decoy_plants = []
    seen_names = {correct_plant.plant_name.lower()} if correct_plant else set()

    # Try to extract decoys from active categories to keep options context-relevant
    categories_shuffled = list(active_categories)
    random.shuffle(categories_shuffled)
    for model_class, extra_filter in categories_shuffled:
        if len(decoy_plants) >= 3:
            break
        query = model_class.query
        if extra_filter is not None:
            query = query.filter(extra_filter)
        
        candidates = query.order_by(db.func.random()).limit(15).all()
        for c in candidates:
            if c.plant_name.lower() not in seen_names:
                decoy_plants.append(c)
                seen_names.add(c.plant_name.lower())
                if len(decoy_plants) >= 3:
                    break

    # If we need more decoys, search across all tables in the database
    if len(decoy_plants) < 3:
        for table in tables:
            if len(decoy_plants) >= 3:
                break
            candidates = table.query.order_by(db.func.random()).limit(15).all()
            for c in candidates:
                if c.plant_name.lower() not in seen_names:
                    decoy_plants.append(c)
                    seen_names.add(c.plant_name.lower())
                    if len(decoy_plants) >= 3:
                        break

    # 3. CONSTRUCT THE GUARANTEED 4-ELEMENT LIST
    final_plants = [None] * 4
    final_plants[target_idx] = correct_plant

    decoy_idx = 0
    for i in range(4):
        if i != target_idx and decoy_idx < len(decoy_plants):
            final_plants[i] = decoy_plants[decoy_idx]
            decoy_idx += 1

    # Extract details safely, guarding against any missing elements
    plant_names = [item.plant_name if item else "Unknown" for item in final_plants]
    plant_image_url = [item.image_url if item else "" for item in final_plants]
    scientific_names = [item.scientific_name if item else "" for item in final_plants]
    plant_types = [item.plant_type if item else "" for item in final_plants]
    source = [item.source if item else "" for item in final_plants]

    return jsonify(
        plant_names=plant_names, 
        plant_image_url=plant_image_url, 
        scientific_names=scientific_names, 
        plant_types=plant_types, 
        source=source, 
        randomIndex=target_idx  # Return target_idx back to frontend so it matches the correct image!
    )

@app.route('/get_county_names')
def get_county_names():
    selected_plant = request.args.get('selected_plant')
    selected_plant = [selected_plant]
    countyNames = []

    # Checks each plant class for the selected plant that also has county data, extracts both
    for table in tables:
        plants_with_counties = db.session.query(table).filter(
            table.location_counties != None, 
            table.plant_name.in_(selected_plant)
        ).all()
        countyNames.extend([(plant.location_counties) for plant in plants_with_counties])
    countyNames = [county.strip() for counties in countyNames for county in counties.split(',')]

    return jsonify(countyNames=countyNames)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
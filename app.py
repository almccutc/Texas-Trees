from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
from sqlalchemy import func
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
        

@app.route('/')
def render_webpage():
    unique_species = [db.session.query(func.count(func.distinct(func.lower(table.plant_name)))).scalar() for table in tables]

    # Retrieve all unique trees with valid URLs (not including bark) to sample from safely
    valid_trees = Trees.query.filter(
        not_(Trees.image_type == 'bark'),
        Trees.image_url != '',
        Trees.image_url.is_not(None)
    ).all()

    # Map trees to their unique names to avoid duplicates
    unique_tree_map = {}
    for tree in valid_trees:
        if tree.plant_name not in unique_tree_map:
            unique_tree_map[tree.plant_name] = tree

    selected_trees = list(unique_tree_map.values())
    random.shuffle(selected_trees)

    # We need exactly 4 unique plant options to populate the landing page safely
    plants_for_home = []
    seen_names = set()

    # Add up to 4 unique trees that have valid image URLs
    for tree in selected_trees:
        if len(plants_for_home) >= 4:
            break
        plants_for_home.append(tree)
        seen_names.add(tree.plant_name.lower())

    # Fallback: If we have fewer than 4 trees with images, fill the remaining slots with any tree names
    if len(plants_for_home) < 4:
        all_trees = Trees.query.all()
        random.shuffle(all_trees)
        for tree in all_trees:
            if len(plants_for_home) >= 4:
                break
            if tree.plant_name.lower() not in seen_names:
                plants_for_home.append(tree)
                seen_names.add(tree.plant_name.lower())

    # Super Fallback: If we still don't have 4, pull from other plant categories
    if len(plants_for_home) < 4:
        for table in tables:
            if len(plants_for_home) >= 4:
                break
            all_plants = table.query.all()
            random.shuffle(all_plants)
            for plant in all_plants:
                if len(plants_for_home) >= 4:
                    break
                if plant.plant_name.lower() not in seen_names:
                    plants_for_home.append(plant)
                    seen_names.add(plant.plant_name.lower())

    # Extract plant names and image URLs from selected data
    plant_names = [item.plant_name for item in plants_for_home]
    plant_image_url = [item.image_url for item in plants_for_home]
    scientific_names = [item.scientific_name for item in plants_for_home]
    plant_types = [item.plant_type for item in plants_for_home]
    source = [item.source for item in plants_for_home]

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

    # Parse and clamp target index to range [0, 3] safely
    try:
        target_idx = int(randomIndex)
        if target_idx < 0 or target_idx > 3:
            target_idx = 0
    except (TypeError, ValueError):
        target_idx = 0

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
            model_class.image_url != '',
            model_class.image_url.is_not(None),
            func.lower(model_class.plant_name) != func.lower(prev_name)
        )
        if extra_filter is not None:
            query = query.filter(extra_filter)
        
        correct_plant = query.order_by(db.func.random()).first()
        if correct_plant:
            break

    # If no matching plant with a valid image is found, search any plant category with an image
    if not correct_plant:
        for table in tables:
            correct_plant = table.query.filter(
                table.image_url != '',
                table.image_url.is_not(None)
            ).order_by(db.func.random()).first()
            if correct_plant:
                break

    # 2. SELECT 3 UNIQUE DECOY PLANTS (Do not require images, just unique names)
    decoy_plants = []
    seen_names = {correct_plant.plant_name.lower()} if correct_plant else set()

    # Try to extract decoys from active categories
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
        randomIndex=randomIndex
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
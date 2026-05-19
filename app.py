from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
from sqlalchemy import func, not_
import os

app = Flask(__name__, static_url_path='/static')

# --- DATABASE CONFIGURATION ---
db_user = os.environ.get('POSTGRES_USER')
db_pw = os.environ.get('POSTGRES_PW')
db_host = os.environ.get('POSTGRES_HOST')
db_name = os.environ.get('POSTGRES_DB')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{db_user}:{db_pw}@{db_host}/{db_name}'
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

    # This custom __init__ is required to support positional arguments in seed scripts
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


def get_base_image_filters(model_class):
    """Keep DB filters lightweight so PostgreSQL can use indexes efficiently."""
    return [
        model_class.image_url.is_not(None),
        model_class.image_url != ''
    ]


def is_valid_image(plant):
    """
    Performs complex string evaluations and disk checks in Python 
    only on the tiny subset of rows we actually intend to use.
    """
    url = plant.image_url
    if not url:
        return False
    
    url_str = str(url).strip()
    url_lower = url_str.lower()
    
    if url_lower in ('', 'none', 'null', 'nan', 'n/a', 'undefined', 'placeholder'):
        return False
        
    if '.' not in url_str:
        return False
        
    if url_lower.startswith(('http://', 'https://')):
        return True
        
    if url_lower.startswith(('/static/', 'static/')):
        relative_path = url_str.lstrip('/')
        return os.path.exists(relative_path)
        
    # Fallback validation for extensions
    return any(url_lower.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg'])


@app.route('/')
def render_webpage():
    # 1. Get counts quickly
    unique_species = [db.session.query(func.count(func.distinct(func.lower(table.plant_name)))).scalar() for table in tables]

    valid_plants = []
    seen_names = set()

    shuffled_tables = list(tables)
    random.shuffle(shuffled_tables)

    # 2. Optimized Sampling: Pull up to 30 random candidates per table instead of ALL rows
    for table in shuffled_tables:
        query = table.query.filter(*get_base_image_filters(table))
        if table == Trees:
            query = query.filter(table.image_type != 'bark')
        
        # PostgreSQL handles the randomization up to a strict limit
        query_results = query.order_by(func.random()).limit(30).all()

        for plant in query_results:
            name_lower = plant.plant_name.lower() if plant.plant_name else ""
            if name_lower and name_lower not in seen_names:
                if is_valid_image(plant):
                    valid_plants.append(plant)
                    seen_names.add(name_lower)
            if len(valid_plants) >= 4:
                break
        if len(valid_plants) >= 4:
            break

    # Mix them up and slice the top 4
    random.shuffle(valid_plants)
    plants_for_home = valid_plants[:4]

    # Extreme Fallback using limited queries
    if len(plants_for_home) < 4:
        for table in shuffled_tables:
            if len(plants_for_home) >= 4:
                break
            all_plants = table.query.order_by(func.random()).limit(10).all()
            for plant in all_plants:
                name_lower = plant.plant_name.lower() if plant.plant_name else ""
                if name_lower and name_lower not in seen_names:
                    plants_for_home.append(plant)
                    seen_names.add(name_lower)
                if len(plants_for_home) >= 4:
                    break

    # Unpack safely
    plant_names = [item.plant_name if item else "Unknown" for item in plants_for_home]
    plant_image_url = [item.image_url if item else "" for item in plants_for_home]
    scientific_names = [item.scientific_name if item else "" for item in plants_for_home]
    plant_types = [item.plant_type if item else "" for item in plants_for_home]
    source = [item.source if item else "" for item in plants_for_home]

    # 3. Optimized Dropdown Query: Fetch ONLY the plant_name column, not whole models
    plant_options = set()
    for TableClass in tables:
        names = db.session.query(TableClass.plant_name).filter(
            TableClass.location_counties != '',
            TableClass.location_counties.is_not(None)
        ).distinct().all()
        for (name,) in names:
            if name:
                plant_options.add(name)

    # Fixed sorting rule to safeguard against empty strings/IndexErrors
    plant_options = sorted(plant_options, key=lambda x: x.split()[0][0].lower() if (x and x.split()) else '')    

    return render_template(
        'index.html', plant_names=plant_names, plant_image_url=plant_image_url, 
        scientific_names=scientific_names, plant_types=plant_types, source=source, 
        unique_species=unique_species, plant_options=plant_options, current_route='render_webpage'
    )


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

    try:
        target_idx = int(randomIndex)
        if target_idx < 0 or target_idx > 3:
            target_idx = random.randint(0, 3)
    except (TypeError, ValueError):
        target_idx = random.randint(0, 3)

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

    if not active_categories:
        active_categories.append((Trees, Trees.image_type == 'close_fullsize'))

    correct_plant = None
    prev_name = previousPlantName.strip().lower() if previousPlantName else ""

    categories_shuffled = list(active_categories)
    random.shuffle(categories_shuffled)
    
    for model_class, extra_filter in categories_shuffled:
        query = model_class.query.filter(
            func.lower(model_class.plant_name) != prev_name,
            *get_base_image_filters(model_class)
        )
        if extra_filter is not None:
            query = query.filter(extra_filter)
        
        candidates = query.order_by(db.func.random()).limit(10).all()
        for candidate in candidates:
            if is_valid_image(candidate):
                correct_plant = candidate
                break
        if correct_plant:
            break

    if not correct_plant:
        for table in tables:
            query = table.query.filter(*get_base_image_filters(table))
            candidates = query.order_by(db.func.random()).limit(10).all()
            for candidate in candidates:
                if is_valid_image(candidate):
                    correct_plant = candidate
                    break
            if correct_plant:
                break

    # Decoys configuration (No images needed, safely using .limit())
    decoy_plants = []
    seen_names = {correct_plant.plant_name.lower()} if correct_plant else set()

    for model_class, extra_filter in categories_shuffled:
        if len(decoy_plants) >= 3:
            break
        query = model_class.query
        if extra_filter is not None:
            query = query.filter(extra_filter)
        
        candidates = query.order_by(db.func.random()).limit(15).all()
        for c in candidates:
            if c.plant_name and c.plant_name.lower() not in seen_names:
                decoy_plants.append(c)
                seen_names.add(c.plant_name.lower())
                if len(decoy_plants) >= 3:
                    break

    if len(decoy_plants) < 3:
        for table in tables:
            if len(decoy_plants) >= 3:
                break
            candidates = table.query.order_by(db.func.random()).limit(15).all()
            for c in candidates:
                if c.plant_name and c.plant_name.lower() not in seen_names:
                    decoy_plants.append(c)
                    seen_names.add(c.plant_name.lower())
                    if len(decoy_plants) >= 3:
                        break

    final_plants = [None] * 4
    final_plants[target_idx] = correct_plant

    decoy_idx = 0
    for i in range(4):
        if i != target_idx and decoy_idx < len(decoy_plants):
            final_plants[i] = decoy_plants[decoy_idx]
            decoy_idx += 1

    return jsonify(
        plant_names=[item.plant_name if item else "Unknown" for item in final_plants], 
        plant_image_url=[item.image_url if item else "" for item in final_plants], 
        scientific_names=[item.scientific_name if item else "" for item in final_plants], 
        plant_types=[item.plant_type if item else "" for item in final_plants], 
        source=[item.source if item else "" for item in final_plants], 
        randomIndex=target_idx  
    )


@app.route('/get_county_names')
def get_county_names():
    selected_plant = request.args.get('selected_plant')
    if not selected_plant:
        return jsonify(countyNames=[])
        
    countyNames = []
    # Case insensitive lookups prevent missing items due to casing mismatches
    for table in tables:
        plants_with_counties = db.session.query(table.location_counties).filter(
            table.location_counties.is_not(None), 
            func.lower(table.plant_name) == selected_plant.strip().lower()
        ).all()
        countyNames.extend([plant.location_counties for plant in plants_with_counties if plant.location_counties])
        
    countyNames = [county.strip() for counties in countyNames for county in counties.split(',') if county.strip()]
    return jsonify(countyNames=countyNames)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
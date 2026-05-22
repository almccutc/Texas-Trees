from flask import Flask, render_template, jsonify, request, make_response, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
from sqlalchemy import func
from sqlalchemy import not_
import os

app = Flask(__name__, static_url_path='/static')

# Flask Secret Key is required to use 'session' to track the last 8 plants
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'plant-quiz-secret-key-1234')

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


def get_random_records(model_class, query, limit=1):
    """
    Fetches random records by sampling IDs in memory. 
    This is massively faster than ORDER BY random() because it avoids 
    forcing the database to sort the entire table.
    """
    # 1. Quickly fetch just the IDs that match the query
    ids = [row[0] for row in query.with_entities(model_class.plant_id).all()]
    if not ids:
        return []
        
    # 2. Pick a random sample of IDs using Python (instantaneous)
    selected_ids = random.sample(ids, min(len(ids), limit))
    
    # 3. Fetch only the specifically chosen rows from the database
    records = model_class.query.filter(model_class.plant_id.in_(selected_ids)).all()
    
    # Shuffle to ensure the resulting list order is also random
    random.shuffle(records) 
    return records


@app.route('/')
def render_webpage():
    unique_species = [db.session.query(func.count(func.distinct(func.lower(table.plant_name)))).scalar() for table in tables]

    valid_plants = []
    seen_names = set()

    # Shuffle tables to ensure a fun, dynamic layout on reload
    shuffled_tables = list(tables)
    random.shuffle(shuffled_tables)

    # Fetch a small random sample directly from DB using the fast ID sampling
    for table in shuffled_tables:
        query = table.query
        if table == Trees:
            # For Trees, we avoid showing 'bark' on the home page for general visual consistency
            query = query.filter(not_(table.image_type == 'bark'))
        
        # Only pull a few random candidates per table instantly
        query_results = get_random_records(table, query, limit=5)

        for plant in query_results:
            name_lower = plant.plant_name.lower()
            if name_lower not in seen_names:
                valid_plants.append(plant)
                seen_names.add(name_lower)

    # Shuffle the pool and take the top 4
    random.shuffle(valid_plants)
    plants_for_home = valid_plants[:4]

    # Extreme fallback
    if len(plants_for_home) < 4:
        for table in shuffled_tables:
            if len(plants_for_home) >= 4:
                break
            fallback_plants = get_random_records(table, table.query, limit=4)
            for plant in fallback_plants:
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

    # Fetch unique plant names directly using column queries (much faster than pulling full rows)
    for TableClass in tables:
        names = db.session.query(TableClass.plant_name).filter(
            TableClass.location_counties != None,
            TableClass.location_counties != ''
        ).distinct().all()
        for row in names:
            plant_options.add(row[0])

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
    # 1. Gather all current switch parameters
    switchState_trees = request.args.get('switchState_trees')
    switchState_leaves = request.args.get('switchState_leaves')
    switchState_barks = request.args.get('switchState_barks')
    switchState_wildflowers = request.args.get('switchState_wildflowers')
    switchState_grasses = request.args.get('switchState_grasses')
    switchState_aquaticplants = request.args.get('switchState_aquaticplants')
    switchState_vines = request.args.get('switchState_vines')
    switchState_cacti = request.args.get('switchState_cacti')
    randomIndex = request.args.get('randomIndex')
    
    try:
        target_idx = int(randomIndex)
        if target_idx < 0 or target_idx > 3:
            target_idx = random.randint(0, 3)
    except (TypeError, ValueError):
        target_idx = random.randint(0, 3)

    # Create a unique string fingerprint of the current switch states to track user changes
    current_switches = f"{switchState_trees}_{switchState_leaves}_{switchState_barks}_{switchState_wildflowers}_{switchState_grasses}_{switchState_aquaticplants}_{switchState_vines}_{switchState_cacti}"

    # --- SESSION QUEUE RETRIEVAL ---
    last_switches = session.get('last_switches')
    pre_fetched_rounds = session.get('pre_fetched_rounds', [])
    recent_plants = session.get('recent_plants', [])
    
    # Backup history logic
    previous_param = request.args.get('previousPlantName')
    if previous_param:
        prev_stripped = previous_param.strip().lower()
        if prev_stripped not in recent_plants:
            recent_plants.append(prev_stripped)
    recent_plants = recent_plants[-8:]

    # If the user changed their filter options, immediately dump the pre-fetched queue
    if current_switches != last_switches:
        pre_fetched_rounds = []
        session['last_switches'] = current_switches

    # Helper functions to save minimal DB Identifiers in the session instead of full objects
    def serialize_plant(plant):
        if not plant: return None
        return {'id': plant.plant_id, 'table': plant.__tablename__}
        
    def fetch_plant_from_cache(data):
        if not data: return None
        table_class = next((t for t in tables if t.__tablename__ == data['table']), None)
        if table_class:
            return table_class.query.get(data['id']) # .get() by ID is near instantaneous!
        return None

    # ==========================================
    # SCENARIO A: WE HAVE PRE-FETCHED ROUNDS!
    # ==========================================
    if pre_fetched_rounds:
        print("[DEBUG] Using instantly PRE-FETCHED round from queue!", flush=True)
        # Pop the first cached round
        round_data = pre_fetched_rounds.pop(0)
        session['pre_fetched_rounds'] = pre_fetched_rounds # Save the queue back
        
        # Load the models using their IDs instantly
        correct_plant = fetch_plant_from_cache(round_data['correct'])
        decoy_plants = [fetch_plant_from_cache(d) for d in round_data['decoys']]

    # ==========================================
    # SCENARIO B: CACHE EMPTY - GENERATE A BATCH
    # ==========================================
    else:
        print("[DEBUG] Queue empty. Batch generating 5 new rounds...", flush=True)
        # Setup active categories based on switches
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

        # Default to Tree + Leaf if nothing is selected
        if not active_categories:
            active_categories.append((Trees, Trees.image_type == 'close_fullsize'))
            active_categories.append((Trees, Trees.image_type == 'leaf'))

        active_tables = list({model_class for model_class, _ in active_categories})
        
        batch_size = 5
        new_rounds = []
        
        # Loop and generate multiple rounds back to back to store in memory
        for _ in range(batch_size):
            correct_plant = None
            categories_shuffled = list(active_categories)
            random.shuffle(categories_shuffled)
            
            # --- Primary Correct Plant Search ---
            for model_class, extra_filter in categories_shuffled:
                query = model_class.query
                if recent_plants:
                    query = query.filter(not_(func.lower(model_class.plant_name).in_(recent_plants)))
                if extra_filter is not None:
                    query = query.filter(extra_filter)
                
                records = get_random_records(model_class, query, limit=1)
                if records:
                    correct_plant = records[0]
                    break

            # --- Fallback Correct Plant Search ---
            if not correct_plant:
                for table in active_tables:
                    query = table.query
                    if recent_plants:
                        query = query.filter(not_(func.lower(table.plant_name).in_(recent_plants)))
                    records = get_random_records(table, query, limit=1)
                    if records:
                        correct_plant = records[0]
                        break
                        
            # --- Extreme Fallback Correct Plant ---
            if not correct_plant:
                for table in active_tables:
                    records = get_random_records(table, table.query, limit=1)
                    if records:
                        correct_plant = records[0]
                        break
                        
            if correct_plant:
                recent_plants.append(correct_plant.plant_name.lower())
                recent_plants = recent_plants[-8:]
                
            # --- Decoy Selection ---
            decoy_plants = []
            seen_names = {correct_plant.plant_name.lower()} if correct_plant else set()
            seen_names.update(recent_plants) # Avoid using recent corrects as decoys
            
            categories_shuffled = list(active_categories)
            random.shuffle(categories_shuffled)
            
            for model_class, extra_filter in categories_shuffled:
                if len(decoy_plants) >= 3:
                    break
                query = model_class.query
                if extra_filter is not None:
                    query = query.filter(extra_filter)
                candidates = get_random_records(model_class, query, limit=10)
                for c in candidates:
                    if c.plant_name.lower() not in seen_names:
                        decoy_plants.append(c)
                        seen_names.add(c.plant_name.lower())
                        if len(decoy_plants) >= 3: break

            # Fallbacks Decoy Search
            if len(decoy_plants) < 3:
                for table in active_tables:
                    if len(decoy_plants) >= 3: break
                    candidates = get_random_records(table, table.query, limit=10)
                    for c in candidates:
                        if c.plant_name.lower() not in seen_names:
                            decoy_plants.append(c)
                            seen_names.add(c.plant_name.lower())
                            if len(decoy_plants) >= 3: break
                            
            # Extreme Fallback Decoy
            if len(decoy_plants) < 3:
                for table in active_tables:
                    if len(decoy_plants) >= 3: break
                    candidates = get_random_records(table, table.query.filter(func.lower(table.plant_name) != func.lower(correct_plant.plant_name)), limit=10)
                    for c in candidates:
                        if c.plant_name.lower() != correct_plant.plant_name.lower() and c not in decoy_plants:
                            decoy_plants.append(c)
                            if len(decoy_plants) >= 3: break

            # Append the minimal ID dicts to our batch
            new_rounds.append({
                'correct': serialize_plant(correct_plant),
                'decoys': [serialize_plant(d) for d in decoy_plants]
            })

        # Save the updated history for future checks
        session['recent_plants'] = recent_plants
        
        # Pop the first round out of the batch for IMMEDIATE use, and cache the remaining ones
        round_data = new_rounds.pop(0)
        session['pre_fetched_rounds'] = new_rounds
        
        # Instantly inflate the chosen immediate round models from the DB
        correct_plant = fetch_plant_from_cache(round_data['correct'])
        decoy_plants = [fetch_plant_from_cache(d) for d in round_data['decoys']]


    if correct_plant:
        print(f"[DEBUG] Setup complete for plant: {correct_plant.plant_name} | Class: {correct_plant.__class__.__name__}", flush=True)

    # Assign correctly into the array based on the target_idx from the frontend
    final_plants = [None] * 4
    final_plants[target_idx] = correct_plant

    decoy_idx = 0
    for i in range(4):
        if i != target_idx and decoy_idx < len(decoy_plants):
            final_plants[i] = decoy_plants[decoy_idx]
            decoy_idx += 1

    plant_names = [item.plant_name if item else "Unknown" for item in final_plants]
    plant_image_url = [item.image_url if item else "" for item in final_plants]
    scientific_names = [item.scientific_name if item else "" for item in final_plants]
    plant_types = [item.plant_type if item else "" for item in final_plants]
    source = [item.source if item else "" for item in final_plants]

    # Use make_response to prevent mobile browser caching
    response = make_response(jsonify(
        plant_names=plant_names, 
        plant_image_url=plant_image_url, 
        scientific_names=scientific_names, 
        plant_types=plant_types, 
        source=source, 
        randomIndex=target_idx
    ))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    
    return response

@app.route('/get_county_names')
def get_county_names():
    selected_plant = request.args.get('selected_plant')
    countyNames = []

    # Query only the location_counties column instead of returning full objects
    for table in tables:
        plants_with_counties = db.session.query(table.location_counties).filter(
            table.location_counties != None, 
            table.plant_name == selected_plant
        ).all()
        countyNames.extend([row[0] for row in plants_with_counties if row[0]])
        
    countyNames = [county.strip() for counties in countyNames for county in counties.split(',')]

    return jsonify(countyNames=countyNames)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
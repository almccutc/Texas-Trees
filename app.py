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
    plants = []
    unique_plant_names = set()

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

    # Select up to 4 unique random tree plants
    sample_size = min(4, len(unique_tree_map))
    selected_trees = random.sample(list(unique_tree_map.values()), sample_size)

    for random_plant in selected_trees:
        plants.append((random_plant.plant_name, random_plant.image_url, random_plant.scientific_name, random_plant.plant_type, random_plant.source))
        unique_plant_names.add(random_plant.plant_name)

    # Extract plant names and image URLs from selected data
    plant_names = [item[0] for item in plants]
    plant_image_url = [item[1] for item in plants]
    scientific_names = [item[2] for item in plants]
    plant_types = [item[3] for item in plants]
    source = [item[4] for item in plants]

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
    plants = []
   
    switchState_trees = request.args.get('switchState_trees')
    switchState_leaves = request.args.get('switchState_leaves')
    switchState_barks = request.args.get('switchState_barks')
    switchState_wildflowers = request.args.get('switchState_wildflowers')
    switchState_grasses = request.args.get('switchState_grasses')
    switchState_aquaticplants = request.args.get('switchState_aquaticplants')
    switchState_vines = request.args.get('switchState_vines')
    switchState_herbs = request.args.get('switchState_herbs')
    switchState_cacti = request.args.get('switchState_cacti')
    randomIndex = request.args.get('randomIndex')
    previousPlantName = request.args.get('previousPlantName')

    # The number of unique plants to retrieve from each table (to prevent duplicates)
    plants_per_table = 4   
    unique_plant_names = set()            
    
    # Helper function modified to accept the model class rather than query object
    def get_quiz_choices(model_class, unique_plant_names, plants_per_table, plants, previousPlantName, extra_filter=None):
        # Always filter out plants that do not have a valid image URL
        query = model_class.query.filter(
            model_class.image_url != '',
            model_class.image_url.is_not(None)
        )
        
        if extra_filter is not None:
            query = query.filter(extra_filter)

        for plantName in range(plants_per_table):
            # Execute the query to retrieve a random plant
            random_plant = query.order_by(db.func.random()).first()

            # Check if the plant name is unique and not the same as the previous plant
            if random_plant and random_plant.plant_name not in unique_plant_names and random_plant.plant_name not in previousPlantName:
                # Append the unique plant to the list
                plants.append((random_plant.plant_name, random_plant.image_url, random_plant.scientific_name, random_plant.plant_type, random_plant.source))
                # Add the plant name to the set of unique names
                unique_plant_names.add(random_plant.plant_name)

        return plants, unique_plant_names
    
    
    if switchState_trees == 'true':
         get_quiz_choices(Trees, unique_plant_names, plants_per_table, plants, previousPlantName, extra_filter=(Trees.image_type == 'close_fullsize'))

    if switchState_leaves == 'true':
         get_quiz_choices(Trees, unique_plant_names, plants_per_table, plants, previousPlantName, extra_filter=(Trees.image_type == 'leaf'))    
    
    if switchState_barks == 'true':
         get_quiz_choices(Trees, unique_plant_names, plants_per_table, plants, previousPlantName, extra_filter=(Trees.image_type == 'bark'))

    if switchState_wildflowers == 'true':
         get_quiz_choices(Flowers, unique_plant_names, plants_per_table, plants, previousPlantName)

    if switchState_vines == 'true':
         get_quiz_choices(Vines, unique_plant_names, plants_per_table, plants, previousPlantName)

    if switchState_cacti == 'true':
         get_quiz_choices(Cacti, unique_plant_names, plants_per_table, plants, previousPlantName)                

    if switchState_grasses == 'true':
         get_quiz_choices(Grasses, unique_plant_names, plants_per_table, plants, previousPlantName)           

    if switchState_aquaticplants == 'true':
         get_quiz_choices(Aquatic, unique_plant_names, plants_per_table, plants, previousPlantName)                                           

    # Selects up to 4 random plant choices for the quiz (safeguarded against population sizes < 4)
    sample_size = min(4, len(plants))
    plants = random.sample(plants, sample_size)    

    plant_names = [item[0] for item in plants]
    plant_image_url = [item[1] for item in plants]
    scientific_names = [item[2] for item in plants]
    plant_types = [item[3] for item in plants]
    source = [item[4] for item in plants]

    return jsonify(plant_names=plant_names, plant_image_url=plant_image_url, scientific_names=scientific_names, plant_types=plant_types, source=source, randomIndex=randomIndex)

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
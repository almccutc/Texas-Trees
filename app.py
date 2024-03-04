from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from secrets_manager import get_secret
from flask import request
import random
from sqlalchemy import func
from sqlalchemy import not_

app = Flask(__name__, static_url_path='/static')

db_config = get_secret()

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql+psycopg2://{db_config["POSTGRES_USER"]}:' +
    f'{db_config["POSTGRES_PW"]}@' +
    f'{db_config["POSTGRES_HOST"]}/' +
    f'{db_config["POSTGRES_DB"]}'
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
    unique_species = []
    unique_plant_names = set()

    unique_species = [db.session.query(func.count(func.distinct(func.lower(table.plant_name)))).scalar() for table in tables]


    # Retrieve 4 unique plants
    while len(plants) < 4:
        # Execute the query to retrieve a random plant
        random_plant = Trees.query.filter(not_(Trees.image_type == 'bark')).order_by(db.func.random()).first()

        # Check if the plant name is unique
        if random_plant.plant_name not in unique_plant_names:
            # Append the unique plant to the list
            plants.append((random_plant.plant_name, random_plant.image_url, random_plant.scientific_name, random_plant.plant_type, random_plant.source))
            
            # Add the plant name to the set of unique names
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
        plants = TableClass.query.filter(TableClass.location_counties != '').all()
        for plant in plants:
            plant_options.add(plant.plant_name)

    plant_options = sorted(plant_options, key=lambda x: x.split()[0][0].lower())    

    return render_template('index.html', plant_names=plant_names, plant_image_url=plant_image_url, scientific_names=scientific_names, plant_types = plant_types, source = source, unique_species = unique_species, plant_options=plant_options, current_route='render_webpage')

@app.route('/plantInfo/')
def render_plant_info():
    # You can add any necessary data processing here
    return render_template('plantInfo.html')

@app.route('/cropData')
def render_crop_data():
    # You can add any necessary data processing here
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

    # The number of unique plants to retrieve from each table (to prevent to duplicates)
    plants_per_table = 4   
    unique_plant_names = set()                     
    
    def get_random_plants(query, unique_plant_names, plants_per_table, plants, previousPlantName, extra_filter='None'):
        unique_plant_names = set()
        
        while len(unique_plant_names) < plants_per_table:
            # Execute the query to retrieve a random plant
            if extra_filter != 'None':
                random_plant = query.filter(extra_filter).order_by(db.func.random()).first()
            else:
                random_plant = query.order_by(db.func.random()).first()

            # Check if the plant name is unique and not the same as the previous plant
            if random_plant and random_plant.plant_name not in unique_plant_names and random_plant.plant_name not in previousPlantName:
                # Append the unique plant to the list
                plants.append((random_plant.plant_name, random_plant.image_url, random_plant.scientific_name, random_plant.plant_type, random_plant.source))
                # Add the plant name to the set of unique names
                unique_plant_names.add(random_plant.plant_name)

        return plants
    
    if switchState_trees == 'true':
        get_random_plants(Trees.query, unique_plant_names, plants_per_table, plants, previousPlantName, extra_filter=(Trees.image_type == 'close_fullsize'))

    if switchState_leaves == 'true':
        get_random_plants(Trees.query, unique_plant_names, plants_per_table, plants, previousPlantName, extra_filter=(Trees.image_type == 'leaf'))    
    
    if switchState_barks == 'true':
        get_random_plants(Trees.query, unique_plant_names, plants_per_table, plants, previousPlantName, extra_filter=(Trees.image_type == 'bark'))

    if switchState_wildflowers == 'true':
        get_random_plants(Flowers.query, unique_plant_names, plants_per_table, plants, previousPlantName)

    if switchState_vines == 'true':
        get_random_plants(Vines.query, unique_plant_names, plants_per_table, plants, previousPlantName)

    if switchState_cacti == 'true':
        get_random_plants(Cacti.query, unique_plant_names, plants_per_table, plants, previousPlantName)                

    if switchState_grasses == 'true':
        get_random_plants(Grasses.query, unique_plant_names, plants_per_table, plants, previousPlantName)           

    if switchState_aquaticplants == 'true':
        get_random_plants(Aquatic.query, unique_plant_names, plants_per_table, plants, previousPlantName)                                           

    # Selects 4 random plant choices for the quiz
    plants = random.sample(plants, 4)    

    plant_names = [item[0] for item in plants]
    plant_image_url = [item[1] for item in plants]
    scientific_names = [item[2] for item in plants]
    plant_types = [item[3] for item in plants]
    source = [item[4] for item in plants]

    return jsonify(plant_names=plant_names, plant_image_url=plant_image_url, scientific_names=scientific_names, plant_types=plant_types, source = source, randomIndex = randomIndex)

@app.route('/get_county_names')
def get_county_names():
    selected_plant = request.args.get('selected_plant')
    selected_plant = [selected_plant]
    countyNames = []

    # Checks each plant class for the selected plant that also county data, extracts both
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

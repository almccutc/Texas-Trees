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

    def __init__(self, plant_name: str, image_type: str, image_url: str, scientific_name: str, plant_type: str, source: str) -> None:
        self.plant_name = plant_name
        self.image_type = image_type
        self.image_url = image_url
        self.scientific_name = scientific_name
        self.plant_type = plant_type
        self.source = source

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
        

@app.route('/')
def render_webpage():
    plants = []
    unique_species = []
    unique_plant_names = set()

    unique_species.append(db.session.query(func.count(func.distinct(func.lower(Trees.plant_name)))).scalar())
    unique_species.append(db.session.query(func.count(func.distinct(func.lower(Flowers.plant_name)))).scalar())
    unique_species.append(db.session.query(func.count(func.distinct(func.lower(Vines.plant_name)))).scalar())
    unique_species.append(db.session.query(func.count(func.distinct(func.lower(Cacti.plant_name)))).scalar())
    unique_species.append(db.session.query(func.count(func.distinct(func.lower(Grasses.plant_name)))).scalar())
    unique_species.append(db.session.query(func.count(func.distinct(func.lower(Aquatic.plant_name)))).scalar())

    # Retrieve 4 unique plants
    while len(plants) < 4:
        # Execute the query to retrieve a random plant
        random_plant = Trees.query.order_by(db.func.random()).first()

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

    return render_template('index.html', plant_names=plant_names, plant_image_url=plant_image_url, scientific_names=scientific_names, plant_types = plant_types, source = source, unique_species = unique_species)

@app.route('/get_plant_name_list')
def get_plant_name_list():
    plants = []
   
    switchState_trees = request.args.get('switchState_trees')
    switchState_wildflowers = request.args.get('switchState_wildflowers')
    switchState_grasses = request.args.get('switchState_grasses')
    switchState_aquaticplants = request.args.get('switchState_aquaticplants')
    switchState_vines = request.args.get('switchState_vines')
    switchState_herbs = request.args.get('switchState_herbs')
    switchState_cacti = request.args.get('switchState_cacti')
    randomIndex = request.args.get('randomIndex')
    previousPlantName = request.args.get('previousPlantName')

    # Define the number of unique plants to retrieve from each table
    plants_per_table = 4

    unique_plant_names = set()

    if switchState_trees == 'true':
        while len(unique_plant_names) < plants_per_table:

            # Execute the query to retrieve a random plant from 'trees'
            random_tree = Trees.query.filter(not_(Trees.image_type == 'bark')).order_by(db.func.random()).first()
            # Check if the plant name is unique
            if random_tree.plant_name not in unique_plant_names and random_tree.plant_name != previousPlantName:
                # Append the unique plant to the list
                plants.append((random_tree.plant_name, random_tree.image_url, random_tree.scientific_name, random_tree.plant_type, random_tree.source))
                
                # Add the plant name to the set of unique names
                unique_plant_names.add(random_tree.plant_name)

    unique_plant_names = set()    
    
    if switchState_wildflowers == 'true':
        while len(unique_plant_names) < plants_per_table:
            # Execute the query to retrieve a random plant from 'flowers'
            random_flower = Flowers.query.order_by(db.func.random()).first()

            # Check if the plant name is unique
            if random_flower.plant_name not in unique_plant_names and random_flower.plant_name != previousPlantName:
                # Append the unique plant to the list
                plants.append((random_flower.plant_name, random_flower.image_url, random_flower.scientific_name, random_flower.plant_type, random_flower.source))
                
                # Add the plant name to the set of unique names
                unique_plant_names.add(random_flower.plant_name)

    unique_plant_names = set()    
    
    if switchState_vines == 'true':
        while len(unique_plant_names) < plants_per_table:
            # Execute the query to retrieve a random plant from 'vines'
            random_vine = Vines.query.order_by(db.func.random()).first()

            # Check if the plant name is unique and not the same as the previous plant
            print(previousPlantName)
            if random_vine.plant_name not in unique_plant_names and random_vine.plant_name != previousPlantName:
                # Append the unique plant to the list
                plants.append((random_vine.plant_name, random_vine.image_url, random_vine.scientific_name, random_vine.plant_type, random_vine.source))
                
                # Add the plant name to the set of unique names
                unique_plant_names.add(random_vine.plant_name)

    unique_plant_names = set()             

    if switchState_cacti == 'true':
        while len(unique_plant_names) < plants_per_table:
            # Execute the query to retrieve a random plant from 'cactus'
            random_cactus = Cacti.query.order_by(db.func.random()).first()

            # Check if the plant name is unique
            if random_cactus.plant_name not in unique_plant_names and random_cactus.plant_name != previousPlantName:
                # Append the unique plant to the list
                plants.append((random_cactus.plant_name, random_cactus.image_url, random_cactus.scientific_name, random_cactus.plant_type, random_cactus.source))
                
                # Add the plant name to the set of unique names
                unique_plant_names.add(random_cactus.plant_name)        

    unique_plant_names = set()             

    if switchState_grasses == 'true':
        while len(unique_plant_names) < plants_per_table:
            # Execute the query to retrieve a random plant from 'grass'
            random_grass = Grasses.query.order_by(db.func.random()).first()

            # Check if the plant name is unique
            if random_grass.plant_name not in unique_plant_names and random_grass.plant_name != previousPlantName:
                # Append the unique plant to the list
                plants.append((random_grass.plant_name, random_grass.image_url, random_grass.scientific_name, random_grass.plant_type, random_grass.source))
                
                # Add the plant name to the set of unique names
                unique_plant_names.add(random_grass.plant_name)  

    unique_plant_names = set()             

    if switchState_aquaticplants == 'true':
        while len(unique_plant_names) < plants_per_table:
            # Execute the query to retrieve a random plant from 'grass'
            random_aquatic = Aquatic.query.order_by(db.func.random()).first()

            # Check if the plant name is unique, previousPlantName
            if random_aquatic.plant_name not in unique_plant_names and random_aquatic.plant_name != previousPlantName:

                # Append the unique plant to the list
                plants.append((random_aquatic.plant_name, random_aquatic.image_url, random_aquatic.scientific_name, random_aquatic.plant_type, random_aquatic.source))
                
                # Add the plant name to the set of unique names
                unique_plant_names.add(random_aquatic.plant_name)                                               

    # Selects 4 random plant choices for the quiz
    plants = random.sample(plants, 4)    

    # Generate options for the plant identification
    plant_names = [item[0] for item in plants]
    plant_image_url = [item[1] for item in plants]
    scientific_names = [item[2] for item in plants]
    plant_types = [item[3] for item in plants]
    source = [item[4] for item in plants]

    print(randomIndex)

    return jsonify(plant_names=plant_names, plant_image_url=plant_image_url, scientific_names=scientific_names, plant_types=plant_types, source = source, randomIndex = randomIndex)
# # Route to retrieve the previous value of a variable or element
# @app.route('/get_previous_value')
# def get_previous_value():
    
#     previous_value = request.args.get('previous_value')

#     # Return the previous value as JSON
#     return jsonify(previous_value=previous_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 

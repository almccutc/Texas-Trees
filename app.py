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

    # Fetch unique plant names from each table
    for TableClass in [Trees, Flowers, Vines, Cacti, Grasses, Aquatic]:
        plants = TableClass.query.filter(TableClass.location_counties != None, TableClass.location_counties != '').all()
        for plant in plants:
            plant_options.add(plant.plant_name)

    plant_options = sorted(plant_options, key=lambda x: x[0])       

    return render_template('index.html', plant_names=plant_names, plant_image_url=plant_image_url, scientific_names=scientific_names, plant_types = plant_types, source = source, unique_species = unique_species, plant_options=plant_options)

@app.route('/get_county_names')
def get_county_names():
    selected_plant = request.args.get('selected_plant')
    selected_plant = [selected_plant]

    plant_classes = [Trees, Flowers, Vines, Cacti, Grasses, Aquatic]

    countyNames = []

    # Checks each plant class for the selected plant that also county data, extracts both
    for plant_class in plant_classes:
        plants_with_counties = db.session.query(plant_class).filter(
            plant_class.location_counties != None, 
            plant_class.plant_name.in_(selected_plant)
        ).all()
        countyNames.extend([(plant.location_counties) for plant in plants_with_counties])
    countyNames = [county.strip() for counties in countyNames for county in counties.split(',')]

    return jsonify(countyNames=countyNames)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 

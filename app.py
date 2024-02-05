from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from secrets_manager import get_secret

import random

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

    def __init__(self, plant_name: str, image_type: str, image_url: str, scientific_name: str, plant_type: str) -> None:
        self.plant_name = plant_name
        self.image_type = image_type
        self.image_url = image_url
        self.scientific_name = scientific_name
        self.plant_type = plant_type

class Trees(BasePlant):
    __tablename__ = 'trees'

class Flowers(BasePlant):
    __tablename__ = 'flower'
        

@app.route('/')
def render_webpage():
    plants = []
    unique_plant_names = set()

    # Retrieve 4 unique plants
    while len(plants) < 4:
        # Execute the query to retrieve a random plant
        random_plant = Trees.query.order_by(db.func.random()).first()

        # Check if the plant name is unique
        if random_plant.plant_name not in unique_plant_names:
            # Append the unique plant to the list
            plants.append((random_plant.plant_name, random_plant.image_url, random_plant.scientific_name, random_plant.plant_type))
            
            # Add the plant name to the set of unique names
            unique_plant_names.add(random_plant.plant_name)

    # Extract plant names and image URLs from selected data
    plant_names = [item[0] for item in plants]
    plant_image_url = [item[1] for item in plants]
    scientific_names = [item[2] for item in plants]
    plant_types = [item[3] for item in plants]

    return render_template('index.html', plant_names=plant_names, plant_image_url=plant_image_url, scientific_names=scientific_names, plant_types = plant_types)

@app.route('/get_plant_name_list')
def get_plant_name_list():
    plants = []
    unique_plant_names = set()

    # Retrieve 2 unique plants from each table (total of 4)
    while len(plants) < 4:
        # Execute the query to retrieve a random plant from 'trees'
        random_tree = Trees.query.order_by(db.func.random()).first()

        # Check if the plant name is unique
        if random_tree.plant_name not in unique_plant_names:
            # Append the unique plant to the list
            plants.append((random_tree.plant_name, random_tree.image_url, random_tree.scientific_name, random_tree.plant_type))
            
            # Add the plant name to the set of unique names
            unique_plant_names.add(random_tree.plant_name)

        # Execute the query to retrieve a random plant from 'flowers'
        random_flower = Flowers.query.order_by(db.func.random()).first()

        # Check if the plant name is unique
        if random_flower.plant_name not in unique_plant_names:
            # Append the unique plant to the list
            plants.append((random_flower.plant_name, random_flower.image_url, random_flower.scientific_name, random_flower.plant_type))
            
            # Add the plant name to the set of unique names
            unique_plant_names.add(random_flower.plant_name)

    # Generate options for the plant identification
    plant_names = [item[0] for item in plants]
    plant_image_url = [item[1] for item in plants]
    scientific_names = [item[2] for item in plants]
    plant_types = [item[3] for item in plants]

    return jsonify(plant_names=plant_names, plant_image_url=plant_image_url, scientific_names=scientific_names, plant_types=plant_types)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from secrets_manager import get_secret

import random

app = Flask(__name__, static_url_path='/static')

db_config = get_secret()
# print((db_config))

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql+psycopg2://{db_config["POSTGRES_USER"]}:' +
    f'{db_config["POSTGRES_PW"]}@' +
    f'{db_config["POSTGRES_HOST"]}/' +
    f'{db_config["POSTGRES_DB"]}'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Plants(db.Model):
    __tablename__ = 'trees'

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

@app.route('/')
def render_webpage():
    all_plant_data = [(plant.plant_name, plant.image_url, plant.scientific_name, plant.plant_type) for plant in Plants.query.all()]
    
    # Randomly select 4 plant data tuples
    selected_plant_data = random.sample(all_plant_data, 4)

    # Extract plant names and image URLs from selected data
    selected_plant_names = [plant_data[0] for plant_data in selected_plant_data]
    selected_plant_image_urls = [plant_data[1] for plant_data in selected_plant_data]
    scientific_names = [plant_data[2] for plant_data in selected_plant_data]
    plant_types = [plant_data[3] for plant_data in selected_plant_data]

    return render_template('index.html', plant_names=selected_plant_names, plant_image_url=selected_plant_image_urls, scientific_names=scientific_names, plant_types = plant_types)

@app.route('/get_plant_name_list')
def get_plant_name_list():
    plants = []

    for _ in range(4):
        # Execute the query to retrieve a random plant
        random_plant = Plants.query.order_by(db.func.random()).first()
        
        # Store the result in the 'plants' list
        plants.append((random_plant.plant_name, random_plant.image_url, random_plant.scientific_name, random_plant.plant_type))

    # Generate options for the plant identification
    plant_names = [item[0] for item in plants]
    plant_image_url = [item[1] for item in plants]
    scientific_names = [item[2] for item in plants]
    plant_types = [item[3] for item in plants]

    return jsonify(plant_names=plant_names, plant_image_url=plant_image_url, scientific_names=scientific_names, plant_types = plant_types)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 

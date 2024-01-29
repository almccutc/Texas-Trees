import os

from flask import Flask, jsonify # calls the Flask component from within the flask package
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
load_dotenv()

import logging

#

app = Flask(__name__, '/static')

@app.route('/')
def render_webpage():
    return render_template('index.html')  

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql+psycopg2://{os.getenv("POSTGRES_USER")}:' +
    f'{os.getenv("POSTGRES_PW")}@' +
    f'{os.getenv("POSTGRES_HOST")}/' +
    f'{os.getenv("POSTGRES_DB")}'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Transaction(db.Model):
    __tablename__ = 'trees'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    amount = db.Column(db.Float)

    def __init__(self, first_name: str, last_name: str, amount: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.amount = amount

    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name} spent {self.amount}'

@app.route('/list_db')
def list_db() -> str:
    transactions = Transaction.query.all()
    if transactions:
        return '\n'.join([str(transaction) for transaction in transactions])
    else:
        return 'No transactions, yet!'

@app.route('/get_plant_name_list')
def get_plant_name_list():

    plants = []

    for _ in range(4):
        cursor = db.cursor()
        # Execute the query to retrieve a random plant
        cursor.execute("SELECT plant_name, plant_url FROM trees ORDER BY RAND() LIMIT 1")
        
        # Fetch the result
        result = cursor.fetchone()

        # Store the result in the 'plants' list
        plants.append(result)

    # Close the database connection
    db.close()

    logging.info(plants)
    # print(plants)

    # Generate options for the plant identification
    plant_names = [item[0] for item in plants]
    image_url = [item[1] for item in plants]

    print(plant_names)
    print(image_url)

    return jsonify(plant_names=plant_names, image_url=image_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

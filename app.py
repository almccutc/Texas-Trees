from flask import Flask, jsonify # calls the Flask component from within the flask package
from flask import render_template
import mysql.connector
import logging

#it worked, try again, try again, try try again#

app = Flask(__name__, '/static')

@app.route('/')
def render_webpage():
    return render_template('index.html')  

@app.route('/get_plant_name_list')
def get_plant_name_list():

    # Set up MySQL connection
    db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='texastreequiz'
)

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

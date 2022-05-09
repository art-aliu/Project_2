from application import app
from flask import Flask
import random


attribute = ['Speed', 'Strength', 'Endurance']

@app.route('/get/attribute')
def get_attribute():
    return random.choice(attribute)

    

 
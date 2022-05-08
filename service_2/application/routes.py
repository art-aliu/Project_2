from application import app 
from flask import Flask, request, Response
import random

attributes = ['Speed', 'Strength', 'Endurance', "Shooting", "Passing", "Tackling"]

@app.route('/attribute', methods=['GET'])
def attribute():
    attribute_selected = random.choice(attributes)
    return Response(f"{attribute_selected}", mimetype='text/plain')
    

 
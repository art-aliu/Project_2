from flask import Flask, request, jsonify
import random

app = Flask(__name__)

Speed = {
    "ratings": {
    0:"Rapid
    1: "Slow"
    2: "Average"
}
}

Strength = {
    "ratings": {
    0: "Very strong"
    1: "Fairly strong"
    2: "Not bad"
    3: "Weak"
}
}


Endurance = {
     "ratings": {
    0: "Elite"
    1: "Decent"
    2: "Milner Quality"
    3: "Woeful"
}
}

Shooting = {
     "ratings": {
    0: "Pinpoint"
    1: "Fairly Accurate"
    2: "Poor"
}
}

Passing = {
     "ratings": {
    0: "Gerrard Quality"
    1: "Standard"
    2: "Cant pass a ball"
}
}

Tackling = {
     "ratings": {
    0: "Van Dijk Quality"
    1: "Monster"
    2: "Good"
    3: "Awful"
}
}

@app.route('/post/status', methods=['POST'])
def post_status():
    physical_attribute = request.jason['physical_attribute']
    skill = request.json['skill']

    if physical_attribute == speed:
        name = random.choice(list(speed["ratings"]. values()))
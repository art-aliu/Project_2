from flask import Flask, request, jsonify, Response
import random

app = Flask(__name__)

rating = {
    'attribute': {
        'Speed': 5
        'Strength': 3
        'Endurance': 2
    },
    'skill': {
        'shooting': 9
        'passing': 8
        'tackling': 8
    }
}


@app.route('/post/rating', method=['POST'])
def post_rating():
    attribute= request.json['Attribute']
    skill = request.json['Skill']

    rating = rating['attribute'[attribute] + rating['skill'][skill]]


    return jsonify(position)



# Speed = { 
#     "ratings": {
#     0:"Rapid
#     1: "Slow"
#     2: "Average"
# }
# }

# Strength = {
#     "ratings": {
#     0: "Very strong"
#     1: "Fairly strong"
#     2: "Not bad"
#     3: "Weak"
# }
# }


# Endurance = {
#      "ratings": {
#     0: "Elite"
#     1: "Decent"
#     2: "Milner Quality"
#     3: "Woeful"
# }
# }

# Shooting = {
#      "ratings": {
#     0: "Pinpoint"
#     1: "Fairly Accurate"
#     2: "Poor"
# }
# }

# Passing = {
#      "ratings": {
#     0: "Gerrard Quality"
#     1: "Standard"
#     2: "Cant pass a ball"
# }
# }

# Tackling = {
#      "ratings": {
#     0: "Van Dijk Quality"
#     1: "Monster"
#     2: "Good"
#     3: "Awful"
# }
# }
from application import app
from flask import Flask, request, jsonify, json, render_template
import random, requests


scout_ratings = {
    'attribute': {
        'Speed': 5,
        'Strength': 3,
        'Endurance' : 2
    },
    'skill': {
        'Shooting': 5,
        'Passing': 3,
        'Tackling': 3
    }
}
@app.route('/post/rating', methods=['POST'])
def post_rating():
    attribute = request.json['attribute']
    skill = request.json['skill']
    
    rating = scout_ratings['attribute'][attribute] + scout_ratings['skill'][skill]

    return jsonify(rating)
    

    




# notes = {0: "Has great potential", 1: "Will never make it"
# special = "Shooting, Passing, Speed"


# @app.route('/extra', method=['POST'])
# def extra():
#     attributes = request.get_json["Attribute"]
#     ratings = request.get_json["Rating"]



#     for special in attributes:
#         if special in get_attribute:
#             return Response(f"{notes[0)}", mimetype = 'text/plain')
#         else:
#             return Response(f"{notes[1)}", mimetype = 'text/plain')
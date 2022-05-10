from application import app
from flask import Flask, request, jsonify, render_template
import random, json


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

@app.route('/post_rating', methods=['POST'])
def post_rating():
    attribute = request.get_json()['attribute']
    skill = request.get_json()['skill']
    
    rating = scout_ratings['attribute'][attribute] + scout_ratings['skill'][skill]
    
    return jsonify(rating)



    # if attribute == 'Speed':
    #     ratings = "5"
    # elif attribute == 'Strength':
    #     ratings = "3"
    # elif attribute == 'Endurance':
    #     ratings = "2"
    # else:
    #     attribute = "Scout likes you"

    # if skill == 'Shooting':
    #     score = "5"
    # elif skill == 'Passing':
    #     score = "3"
    # elif skill == 'Tackling':
    #     score = '3'
    # else:
    #     skill = "World Class"

    # overall_scout_rating = { 
    #     "ratings": ratings,
    #     "score": score
    #    }

    # return jsonify(overall_scout_rating)

    



from application import app
from flask import Flask, render_template, jsonify, Response, request
import requests, json


@app.route('/')
def home():
    attribute = requests.get('http://service_2:5000/get/attribute').text
    skill = requests.get('http://service_3:5000/get/skill').text

    content = {'attribute': attribute, 'skill': skill}

    rating = requests.post('http://service_4:5000/post/rating', json=content) 

    final_rating = f"This player has '{attribute}', and '{skill}' and therefore gets a scout rating of '{rating.text}'"

    return render_template('home.html', attribute=attribute, skill=skill, rating=rating, final_rating=final_rating)
   
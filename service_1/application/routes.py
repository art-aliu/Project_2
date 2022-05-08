from application import app
from flask import Flask, render_template, jsonify, Response
import requests


@app.route('/')
def home():
    attribute_generated = requests.get('http://service_2:5000/attribute')
    rating_generated = requests.get('http://service_3:5000/rating')

    # content = {'attribute': attribute, 'skill': skill}
    final_score = requests.post('http://service_4:5000/extra')
    
    # final_rating = f"Rating '{attribute_generated.text}', gets a scout rating of '{rating_generated.text}' and a comment of '{final_score.text}'"

    return render_template('home.html', final_rating=final_rating)


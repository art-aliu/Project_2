from application import app
from flask import render_template, redirect, url_for, request, jsonify, json
import requests


@app.route('/', methods=["POST", "GET"])
def index():
    attribute = requests.get('http://service-2:5000/get/Attribute').text
    skill = requests.get('http://service-3:5000/get/Skill').text

    content = {'attribute': attribute, 'skill': skill}
    rating = requests.post('http://service-4:5000/post/rating', json=rating).json()
    
    records = Footballer.query.order_by(Footballer.id.desc()).limit(15).all()

    outcome = Footballer(attribute=attribute, skill=skill, rating=rating)
    db.session.add(outcome)
    db.session.commit()
    data = Footballer.query.all()

    return render_template('index.html', outcome=outcome, attribute=attribute, skill=skill, rating=rating, data=data)


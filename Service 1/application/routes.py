from application import app, db
from application.models import Attribute
from flask import render_template, redirect, url_for, request
import requests, json


@app.route('/', methods=["POST", "GET"])
def index():
    attribute = requests.get('http://service-2:5000/get/Attribute').text
    skill = requests.get('http://service-3:5000/get/Skill')

    # content = {'attribute': attribute, 'skill': skill}
    # status = requests.post('http://service-4:5000/post/status', json=content).json()

    new_attribute = Attribute(speed=speed, strength=strength, skill=skill, position=position)

    # context = db.session.query(Attribute).order_by(Attribute.id.desc()).first()

    # if new_attribute:
    #     db.session.add(new_attribute)
    #     db.session.commit()

        statement = f"You have generated a {attribute} with a football skills {skill} and therefore the preferred position for this player would be {position}

        return render_template('index.html', statement=statement, context=context)


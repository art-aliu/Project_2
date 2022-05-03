from application import app, db
from application.models import Physical_Attribute
from flask import render_template, redirect, url_for, request
import requests, json


@app.route('/', methods=["POST", "GET"])
def index():
    physical_attribute = requests.get('http://service-2:5000/get/Physical_Attribute').text
    skill = requests.get('http://service-3:5000/get/Skill').json()

    content = {'physical_attribute': physical_attribute, 'skill': skill}
    status = requests.post('http://service-4:5000/post/status', json=content).json()

    context = db.session.query(Physical_Attribute).order_by(Physical_Attribute.id.desc()).first()

     if new_physical_attribute:
        db.session.add(new_physical_attribute)
        db.session.commit()

        statement = f"You have generated a {physical_attribute} with a football skills {skill} and therefore the preferred position for this player would be {position}

        return render_template('index.html', statement=statement, context=context)


from application import app
from flask import Flask, Response 
import random

skill = ["Shooting", "Passing", "Tackling"]

@app.route('/get/skill')
def get_skill():
    return random.choice(skill)

    

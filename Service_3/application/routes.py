from application import app 
from flask import Flask, request, Response 
import random

app = Flask(__name__)


@app.route('/get_skill',methods=['GET'])
def name(): 
    skill_choice = ["Shooting", "Passing", "Tackling", "Reflexes"]
    skill_name = random.choice(skill_choice)
    return Response(f"{skill_name}", mimetype="text/plain")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')

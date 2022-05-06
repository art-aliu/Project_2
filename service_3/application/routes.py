from application import app 
from flask import Flask
import random

app = Flask(__name__)


skill = ["Shooting", "Passing", "Tackling"]

@app.route('/get_skill',methods=['GET'])
def get_skill(): 
    return random.choice(skill)
    
# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

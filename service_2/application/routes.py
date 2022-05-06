from application import app 
from flask import Flask 
import random

app = Flask(__name__)

attribute= ['Speed', 'Strength', 'Endurance']

@app.route('/get_attribute', methods = ['GET'])
def get_attribute():
    return random.choice(attribute)
    
    
# if __name__ == '__main__':
#     app.run(debug=True,port=5000,host='0.0.0.0')

 
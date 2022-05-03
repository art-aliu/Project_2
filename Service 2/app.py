from flask import Flask
import random

app = Flask(__name__)

physical_attribute = ['Speed', 'Strength', 'Endurance', 'Shooting', 'Passing', 'Tackling']

@app.route('/get/physical_attribute')
def get_physical_attribute():
    return random.choice(physical_attribute)
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')

 
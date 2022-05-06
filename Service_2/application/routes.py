from application import app 
from flask import Flask, request, Response 
import random

app = Flask(__name__)

@app.route('/get_attribute', methods = ['GET'])
def name():
    attribute_choice = ['Speed', 'Strength', 'Endurance']
    attribute_name = random.choice(attribute_choice)
    return Response(f"{attribute_name}", mimetype="text/plain")
    
    
# if __name__ == '__main__':
#     app.run(debug=True,port=5000,host='0.0.0.0')

 
from flask import Flask
import random

app = Flask(__name__)

@app.route('/get/skill')
def get_skill():
    return jsonify(random.randint(1, 99))

if __name__ == '__main__':
    app.run(host='0.0.0.0')


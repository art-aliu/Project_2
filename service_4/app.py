from flask import Flask, request, jsonify
import random

app = Flask(__name__)


if __name__ == '__main__':
    app.run(port = 5000, host = '0.0.0.0')

    
from flask import Flask, request, jsonify
import random
from application import app


if __name__ == '__main__':
    app.run(port = 5000, host = '0.0.0.0')

    
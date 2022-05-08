from application import app
from flask import Flask, request, jsonify, Response
import requests

notes = {0: "Has great potential", 1: "Will never make it"
special = "Shooting, Passing, Speed"


@app.route('/extra', method=['POST'])
def extra():
    get_attribute= request.get['attribute']

    for special in get_attribute:
        if special in get_attribute:
            return Response(f"{notes[0)}", mimetype = 'text/plain')
        else:
            return Response(f"{notes[1)}", mimetype = 'text/plain')



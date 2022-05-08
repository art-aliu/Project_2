from application import app 
from flask import Flask, Response, request
import random

ratings = ["Five Stars", "Four Stars", "Three Stars", "Two Stars", "One Star"]

@app.route('/rating', methods = ['GET'])
def rating(): 
    rating_selected = random.choice(ratings)
    return Response(f"(rating_selected)", mimetype='text/plain')
    

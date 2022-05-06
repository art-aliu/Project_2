from . import db


class Footballer(db.model):
    id = db.Column(db.Integer, primary_key=True)
    attribute = db.Column(db.String(50))
    skill = db.Column(db.String(50))
    rating = db.Column(db.Float)

db.create_all()


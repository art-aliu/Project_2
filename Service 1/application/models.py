from application import db


class Attribute(db.model):
    id = db.Column(db.Integer, primary_key=True)
    speed = db.Column(db.String(20))
    strength = db.Column(db.String(50))
    endurance = db.Column(db.String(20))
    skill = db.Column(db.String(20))
    position = db.Column(db.String(20))
    # tackling = db.Column(db.String(20))
    # shooting = db.Column(db.String(20))
    # passing = db.Column(db.String(20))
    
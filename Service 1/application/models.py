from . import db

class Physical_Attribute(db.model):
    id = db.Column(db.Integer, primary_key=True)
    speed = db.Column(db.String(20))
    strength = db.Column(db.String(50))
    endurance = db.Column(db.String(50))
    skill = db.Column(db.Integer, )
    # tackling = db.Column(db.String(20))
    # shooting = db.Column(db.String(20))
    # passing = db.Column(db.String(20))
    
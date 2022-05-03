from flask inmport flask
from flask_sqlachemy import SQLALchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes
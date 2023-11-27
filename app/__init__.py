from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
print(sys.path)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jaredp:secret@localhost/strongapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import routes

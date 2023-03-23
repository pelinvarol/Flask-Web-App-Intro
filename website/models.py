from . import db 
# db is sqlalchemy object we created for the database 
from flask_login import UserMixin
from datetime import datetime


# func gets current date and time 
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# a database model is just a layout or a blueprint for an object that's going to be stored in the database
# all the users have to conform to this model
class User(db.Model, UserMixin):
    # COLUMN() define the type of column
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    notes = db.relationship('Note') # !!! CAPITAL LETTER NEEDED FOR A RELATIONSHIP !!!
    #  The user has many notes. This code tells flask and sql alchemy that do your magic and every time we create a note, add into this
    # user's notes relationship that Note ID. This relationship will be a list and it'll store all of the different notes


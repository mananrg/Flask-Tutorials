import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
#setting the database location i.e tells the app about the database location
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # by default its true
db=SQLAlchemy(app)



class Puppy(db.Model):
#class name will be set as table name
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Text)

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year/s old"

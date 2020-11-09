# models.py
import flask_sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float, PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import *

from app import db

class Users(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Text)
    gender = db.Column(db.String(5))
    activityLevel = db.Column(db.Text)
    height = db.Column(db.Integer)
    weight = db.relationship('Weight', backref = 'users')
    
    # db.session.add(models.Users(email, name, age, gender, activityLevel))
    def __init__(self, email, name, height, age, gender, activityLevel):
        self.id = email
        self.name = name
        self.height = height
        self.age = age
        self.gender = gender
        self.activityLevel = activityLevel
        
    def __repr__(self):
        return '<Email: %s\nName: %s\nHeight: %s\nAge: %s\nGender: %s\nActivity Level: %s>' % (self.id, self.name, self.height, self.age, self.gender, self.activityLevel)
        
class Weight(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    email = db.Column(db.String(50), db.ForeignKey('users.id'))
    
    # db.session.add(models.Weight(weight, email))
    def __init__(self, weight, email):
        self.weight = weight
        self.email = email
        
    def __repr__(self):
        return '<Weight: %s\n User: %s>' % (self.weight, self.email)

db.create_all()
db.session.commit()
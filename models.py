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
    measurements = db.relationship('Measurements', backref = 'users')
    
    def __init__(self, email, name):
        self.id = email
        self.name = name
        
    def __repr__(self):
        return '<Email: %s\nName: %s>' % (self.id, self.name)
        
class Measurements(db.Model):
    __table_args__ = {'extend_existing': True}
    mType = db.Column(db.String(20), primary_key=True)
    value = db.Column(db.Integer)
    email = db.Column(db.String(50), db.ForeignKey('users.id'))
    
    def __init__(self, mType, value, email):
        self.mType = mType
        self.value = value
        self.email = email
        
    def __repr__(self):
        return '<Type: %s\nValue: %s\nUser: %s>' % (self.mType, self.value, self.email)
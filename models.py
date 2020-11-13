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

class Macros(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    bmr = db.Column(db.Float)
    max_cal = db.Column(db.Float)
    min_cal = db.Column(db.Float)
    max_prot = db.Column(db.Float)
    min_prot = db.Column(db.Float)
    max_carb = db.Column(db.Float)
    min_carb = db.Column(db.Float)
    max_fat = db.Column(db.Float)
    min_fat = db.Column(db.Float)
    email = db.Column(db.String(50), db.ForeignKey('users.id'))
    
    # db.session.add(models.Weight(weight, email))
    def __init__(self, bmr, max_cal, min_cal, max_prot, min_prot, max_carb, min_carb, max_fat, min_fat, email):
        self.bmr = bmr
        self.max_cal = max_cal
        self.min_cal = min_cal
        self.max_prot = max_prot
        self.min_prot = min_prot
        self.max_carb = max_carb
        self.min_carb = min_carb
        self.max_fat = max_fat
        self.min_fat = min_fat
        self.email = email
        
    def __repr__(self):
        return '<Bmr: %s\n Max Calories: %s\n Min Calories: %s\n Max Protein: %s\n Min Protein: %s\n Max Carbs: %s\n Min Carbs: %s\n Max Fat: %s\n Min Fat: %s\n User: %s>' % (self.bmr, 
        self.max_cal, self.min_cal, self.max_prot, self.min_prot, self.max_carb, self.min_carb, self.max_fat, self.min_fat, self.email)

class Meals(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    breakfast = db.Column(db.Text)
    lunch = db.Column(db.Text)
    dinner = db.Column(db.Text)
    meal_cal = db.Column(db.Float)
    meal_carb = db.Column(db.Float)
    meal_prot = db.Column(db.Float)
    meal_fat = db.Column(db.Float)
    email = db.Column(db.String(50), db.ForeignKey('users.id'))
    
    # db.session.add(models.Weight(weight, email))
    def __init__(self, breakfast, lunch, dinner, meal_cal, meal_carb, meal_prot, meal_fat, email):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
        self.meal_cal = meal_cal
        self.meal_carb = meal_carb
        self.meal_prot = meal_prot
        self.meal_fat = meal_fat
        self.email = email
        
    def __repr__(self):
        return '<Breakfast: %s\n Lunch: %s\n Dinner: %s\n Meal Calories: %s\n Meal Carbs: %s\n Meal Protein: %s\n Meal Fat: %s\n User: %s>' % (self.breakfast,
        self.lunch, self.dinner, self.meal_cal, self.meal_carb, self.meal_prot, self.meal_fat, self.email)

db.create_all()
db.session.commit()
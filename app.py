from os.path import join, dirname
from dotenv import load_dotenv
import os, flask, flask_sqlalchemy, flask_socketio, datetime, pytz
from flask import request
from sqlalchemy import func

from calories_count import bmr_cal,daily_caloric_need,calculate_macro
from spoonacular import foodsearch, mealplan

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


DOTENV_PATH = join(dirname(__file__), "sql.env")
load_dotenv(DOTENV_PATH)

DATABASE_URI = os.environ["DATABASE_URL"]

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app
db.create_all()
db.session.commit()
import models


def get_user_details(user_email):
    db_users=[\
        db_user for db_user\
        in db.session.query(models.Users).all()
        ]
    for user in db_users:
        if(user.id == user_email):
            current_user=user
            break
    macros=db.session.query(models.Macros).filter_by(email=current_user.id).scalar()
    meals=db.session.query(models.Meals).filter_by(email=current_user.id).scalar()

    print("current_user",current_user)
    print("current_user[height]",current_user.height)
    user_details = {
        'id':current_user.id,
        'height': current_user.height,
        'age': current_user.age,
        'gender':current_user.gender,
        'activityLevel': current_user.activityLevel,
        'bmr' : macros.bmr,
        'maxCal' : macros.max_cal,
        'maxProt' : macros.max_prot,
        'maxCarb' : macros.max_carb,
        'maxFat' : macros.max_fat,
        'breakfastMeal' : meals.breakfast,
        'lunchMeal' : meals.lunch,
        'dinnerMeal' : meals.dinner,
        'calMeal' : meals.meal_cal,
        'carbMeal' : meals.meal_carb,
        'protMeal' : meals.meal_prot,
        'fatMeal' : meals.meal_fat
    }
    socketio.emit('profile details', user_details)
    print(user_details)
# def get_most_recent_weight(user_email, sid):
#     recent = str(db.session.query(models.Weight).filter_by(email = user_email).first().weight)
#     print('\nweight' + recent)
#     socketio.emit('most recent weight', {
#         'recentWeight': recent,
#         'sid': sid
#     })
    
# @socketio.on('new entry')
# def on_new_entry(data):
#     db.session.add(models.Weight(data['weight'], data['email']))
#     db.session.commit()
#     get_most_recent_weight(data['email'], data['sid'])
    
@socketio.on('new food search')
def on_new_food_search(data):
    food_name = {
        'food': data['food_search']
    }
    
    
    food_response=foodsearch(food_name['food'])
    socketio.emit('food response',food_response)
@socketio.on('new user input')
def on_new_user(data):
    
    measurements = {
        'height': data['height'],
        'weight': data['weight'],
        'age': data['age'],
        'gender': data['gender'],
        'activityLevel': int(data['activityLevel'][0])
    }
    googleUsr = {
        'name': data['name'],
        'email': data['email'],
        'sid': request.sid
    }
    bmr=bmr_cal(measurements['weight'],measurements['height'],measurements['age'],measurements['gender'])
    print("Your Estimated Basal Metabolic Rate is " + str(bmr) + ".")
    calories=daily_caloric_need(bmr,measurements['activityLevel'])
    print(calories)
    macros=calculate_macro(calories)
    print(macros)
    meals=mealplan(calories)
    print(meals)
    profile_data={
        'weight': data['weight'],
        'activityLevel': data['activityLevel'],
        'gainOrLose': data['gainOrLose'],
        'MaxCalories': macros['MaxCalories']
        
    }
    
    #To fetch the recepies from API getting the variable ready
    
    db.session.add(models.Users(googleUsr['email'], googleUsr['name'], measurements['height'], measurements['age'], measurements['gender'], measurements['activityLevel']))
    db.session.commit()

    db.session.add(models.Macros(bmr, macros['MaxCalories'], macros['MinCalories'], macros['MaxProtein'], macros['MinProtein'], macros['MaxCarbs'], macros['MinCarbs'], macros['MaxFat'], macros['MinFat'], googleUsr['email']))
    db.session.commit()
    
    db.session.add(models.Meals(meals['breakfast'], meals['lunch'], meals['dinner'], meals['nutrients']['calories'], meals['nutrients']['carbohydrates'], meals['nutrients']['protein'], meals['nutrients']['fat'], googleUsr['email']))
    db.session.commit()

    db.session.add(models.Weight(measurements['weight'], googleUsr['email']))
    db.session.commit()
        
    print(
            "Created db Entry for "
            + googleUsr["name"]
            + " with email "
            + googleUsr["email"]
        )
    socketio.emit('success login', googleUsr)
    socketio.emit('is not logging in', '')
    get_user_details(googleUsr['email'])
    #get_most_recent_weight(googleUsr['email'], googleUsr['sid'])
    
     
@socketio.on('google sign in')
def on_google_sign_in(data):
    googleUsr = { 
        'name': data['name'],
        'email': data['email'],
        'sid': request.sid
    }
    if db.session.query(models.Users.id).filter_by(id = googleUsr['email']).scalar() is None:
        print('New User: ' + googleUsr['name'])
        socketio.emit('is logging in', {
            'res': 'User is attempting to login',
            'sid': request.sid
        })
        socketio.emit('new form', googleUsr)
    else:
        print("Welcome Back! " + googleUsr["name"])
        socketio.emit('success login', googleUsr )
        get_user_details(googleUsr['email'])
        #get_most_recent_weight(googleUsr['email'], googleUsr['sid'])

@socketio.on('new food_search')

@socketio.on("connect")
def on_connect():
    print('\nConnected')

@socketio.on("disconnect")
def on_disconnect():
    print('\nDisconnected')

@app.route("/")
def home():
    return flask.render_template("home.html")
    
@app.route("/profile")
def profile():
    return flask.render_template("profile.html")

@app.route("/foodsearch")
def food_search():
    return flask.render_template("foodSearch.html") 

if __name__ == '__main__': 
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True,
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
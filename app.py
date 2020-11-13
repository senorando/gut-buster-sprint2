from os.path import join, dirname
from dotenv import load_dotenv
import os, flask, flask_sqlalchemy, flask_socketio, datetime, pytz
from flask import request
from sqlalchemy import func
import models
from calories_count import bmr_cal,daily_caloric_need,calculate_macro
from spoonacular import foodsearch

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

@socketio.on('new user input')
def get_user_details(user_email):
    db_users=[\
        db_user for db_user\
        in db.session.query(models.Users).all()
        ]
    for user in db_users:
        if(user.id == user_email):
            current_user=user
            break
    
    print("current_user",current_user)
    print("current_user[height]",current_user.height)
    user_details = {
        'id':current_user.id,
        'height': current_user.height,
        'age': current_user.age,
        'gender':current_user.gender,
        'activityLevel': current_user.activityLevel,
    }
    socketio.emit('profile details', user_details)

@socketio.on('new food search')
def on_new_food_search(data):
    food_name = {
        'food': data['food_search']
    }
    
    
    food_response=foodsearch(food_name['food'])
    print(food_response)
    
    
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
    #possible socket to client stating bmr
    
    
    #daily calories needs
    calories=daily_caloric_need(bmr,measurements['activityLevel'])
    
    print(calories)
    macros=calculate_macro(calories)
    print(macros)
   
   
   
    profile_data={
        'weight': data['weight'],
        'activityLevel': data['activityLevel'],
        'gainOrLose': data['gainOrLose'],
        'MaxCalories': macros['MaxCalories']
        
    }
    
    
    #To fetch the recepies from API getting the variable ready
       
    db.session.add(models.Users(googleUsr['email'], googleUsr['name'], measurements['height'], measurements['age'], measurements['gender'], measurements['activityLevel']))
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
    
# @socketio.on ()
#     socketio.emit('is editing','')
    
     
@socketio.on('google sign in')
def on_google_sign_in(data):
    googleUsr = { 
        'name': data['name'],
        'email': data['email'],
        'sid': request.sid
    }
    if db.session.query(models.Users.id).filter_by(id = googleUsr['email']).scalar() is None:
        print('New User: ' + googleUsr['name'])
        socketio.emit('is logging in', 'User is attempting to login')
        socketio.emit('new form', googleUsr)
    else:
        print("Welcome Back! " + googleUsr["name"])
        socketio.emit('success login', googleUsr )
        get_user_details(googleUsr['email'])

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
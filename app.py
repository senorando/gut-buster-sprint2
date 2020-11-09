from os.path import join, dirname
from dotenv import load_dotenv
import os, flask, flask_sqlalchemy, flask_socketio, datetime, pytz
from flask import request
from sqlalchemy import func
import models
#import calories_count

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

@socketio.on('new user input')
def on_new_user(data):
    measurements = {
        'height': data['height_inch'],
        'weight': data['weight'],
        'age': data['age'],
        'gender': data['gender'],
        'activityLevel': data['activityLevel']
    }
    googleUsr = {
        'name': data['name'],
        'email': data['email']
    }
    badResponse = 'Bad '
    if not measurements['height'].isnumeric():
        badResponse += 'height, '
    if not measurements['weight'].isnumeric():
        badResponse += 'weight, '
    if not measurements['age'].isnumeric():
        badResponse += 'age, '
    if not measurements['gender'].lower() == 'man' or measurements['gender'].lower() == 'woman':
        print(measurements['gender'].lower())
        badResponse += 'gender, '
    if not measurements['activityLevel'].isnumeric():
        badResponse += 'activity level'
        
    if len(badResponse) >= 4:
       
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
    else:
        print(badResponse)
        socketio.emit('fail login', {
            'response': badResponse
        })

@socketio.on('google sign in')
def on_google_sign_in(data):
    googleUsr = { 
        'name': data['name'],
        'email': data['email']
    }
    if db.session.query(models.Users.id).filter_by(id = googleUsr['email']).scalar() is None:
        print('New User: ' + googleUsr['name'])
        socketio.emit('new form', { 
            'response': 'User must fill in form'
            })
    else:
        print("Welcome Back! " + googleUsr["name"])
        socketio.emit('success login', googleUsr )

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
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
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


@socketio.on('google sign in')
def on_google_sign_in(data):
    google_usr = { 
        'name': data['name'],
        'email': data['email']
    }
    db.session.add(models.Users( google_usr['email'], google_usr['name'] ))
    db.session.commit()

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
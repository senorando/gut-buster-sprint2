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
        
    weightInKgs =  measurements['weight'] / 2.2
    heightInCentimeters = measurements['height'] * 2.54
    if measurements['gender'].lower() == "men":
        bmr = int((10 * weightInKgs) 
        + (6.25 * heightInCentimeters ) - (5 * data['age'] ) + 5)
    elif measurements['gender'].lower() =="women":
        bmr = int((10 * weightInKgs) 
        + (6.25 * heightInCentimeters ) - (5 * data['age'] ) - 161)
    
    print("Your Estimated Basal Metabolic Rate is " + str(bmr) + ".")
    #possible socket to client stating bmr
    
    #daily calories needs
    
    if measurements['activityLevel'] == 1:
        activityLevelIndex = 1.2
    elif measurements['activityLevel'] == 2:
        activityLevelIndex = 1.375
    elif measurements['activityLevel'] == 3:
        activityLevelIndex = 1.46
    elif measurements['activityLevel'] == 4:
        activityLevelIndex = 1.725
    elif measurements['activityLevel'] == 5:
        activityLevelIndex = 1.9
    
    dailyCaloriesNeeded = int(bmr * activityLevelIndex)
    print("Based on the BMR to maintain your current weight you need: " + str(dailyCaloriesNeeded) + " calories a day ")
    #possible socket to client stating daily calorie needs
    calories=dailyCaloriesNeeded
    
    calories_from_protein = int(.4 * calories)
    calories_in_protein = int(calories_from_protein / 4)
    calories_from_carbs = int(.4 * calories)
    calories_in_carbs = int(calories_from_carbs / 4)
    calories_from_fat = int(.2 * calories)
    calories_in_fat =int(calories_from_fat / 9)
    
    print("Calories from Protein: " + str(calories_from_protein))
    print("Grams of Protein: " + str(calories_in_protein))
    print("Calories from Carbs: " + str(calories_from_carbs))
    print("Grams of Carbs: " + str(calories_in_carbs))
    print("Calories from Fat: " + str(calories_from_fat))
    print("Grams of Fat: " + str(calories_in_fat))
    #possible socket to client statinghow much protein/carbs/fat they need to maintain weight
    
    #calculate fat loss / gain
    # 1 lb pf fat has 3500 calories to lose .5 lbs a week, divide 3,500 in half and then divide by 7
    halfAPoundaWeek_calories =int(calories - int((3500 / 2) / 7 ))
    print("\n")
    print("To lose .5 lb of fat a week your daily calories needs to drop to:  " + str(halfAPoundaWeek_calories) + ". ")

    calories_from_protein = int(.4 * halfAPoundaWeek_calories)
    calories_in_protein = int(calories_from_protein / 4)
    calories_from_carbs = int(.4 * halfAPoundaWeek_calories)
    calories_in_carbs = int(calories_from_carbs / 4)
    calories_from_fat = int(.2 * halfAPoundaWeek_calories)
    calories_in_fat =int(calories_from_fat / 9)

    print("Calories from Protein: " + str(calories_from_protein))
    print("Grams of Protein: " + str(calories_in_protein))
    print("Calories from Carbs: " + str(calories_from_carbs))
    print("Grams of Carbs: " + str(calories_in_carbs))
    print("Calories from Fat: " + str(calories_from_fat))
    print("Grams of Fat: " + str(calories_in_fat))
     #possible socket to client statinghow much protein/carbs/fat they need to loose weight
    
    
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
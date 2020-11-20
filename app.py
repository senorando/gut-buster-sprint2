'''app.py'''
# pylint: disable=C0116
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=W0612
from os.path import join, dirname
from dotenv import load_dotenv
import os, flask, flask_sqlalchemy, flask_socketio, datetime
from flask import request
from calories_count import bmr_cal, daily_caloric_need, calculate_macro
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

online_users = []

def get_user_details(user_email):
    db_users = [db_user for db_user in db.session.query(models.Users).all()]
    for user in db_users:
        if user.id == user_email:
            current_user = user
            break
    macros = db.session.query(models.Macros).filter_by(email=current_user.id).scalar()

    print("current_user", current_user)
    print("current_user[height]", current_user.height)
    date = str(datetime.datetime.now().date())
    lastlogin = str(db.session.query(models.Users.date).all())
    lastlogin = lastlogin.replace('[(\'','')
    lastlogin = lastlogin.replace('\',)]','')
    print("last login", lastlogin)
    login= "2020-11-20"
    calories = str((db.session.query(models.Macros.max_cal).filter_by(email=current_user.id).all()))
    calories = calories.replace('[(','')
    calories = calories.replace(',)]','')
    #print(calories)
    if date > login:
        newmeal = mealplan(calories)
        meal = db.session.query(models.Meals).get(1)
        meal.breakfast=newmeal["breakfast"],
        meal.lunch=newmeal["lunch"],
        meal.dinner=newmeal["dinner"],
        meal.meal_cal=newmeal["nutrients"]["calories"],
        meal.meal_carb=newmeal["nutrients"]["carbohydrates"],
        meal.meal_prot=newmeal["nutrients"]["protein"],
        meal.meal_fat=newmeal["nutrients"]["fat"],
        meal.email=current_user.id,
        db.session.commit()
        user_details = {
            "id": current_user.id,
            "height": current_user.height,
            "age": current_user.age,
            "gender": current_user.gender,
            "activityLevel": current_user.activityLevel,
            "bmr": macros.bmr,
            "maxCal": macros.max_cal,
            "maxProt": macros.max_prot,
            "maxCarb": macros.max_carb,
            "maxFat": macros.max_fat,
            "breakfastMeal": meal.breakfast,
            "lunchMeal": meal.lunch,
            "dinnerMeal": meal.dinner,
            "calMeal": meal.meal_cal,
            "carbMeal": meal.meal_carb,
            "protMeal": meal.meal_prot,
            "fatMeal": meal.meal_fat,
        }
        socketio.emit("profile details", user_details)
    else:
        meals = db.session.query(models.Meals).filter_by(email=current_user.id).scalar()
        user_details = {
            "id": current_user.id,
            "height": current_user.height,
            "age": current_user.age,
            "gender": current_user.gender,
            "activityLevel": current_user.activityLevel,
            "bmr": macros.bmr,
            "maxCal": macros.max_cal,
            "maxProt": macros.max_prot,
            "maxCarb": macros.max_carb,
            "maxFat": macros.max_fat,
            "breakfastMeal": meals.breakfast,
            "lunchMeal": meals.lunch,
            "dinnerMeal": meals.dinner,
            "calMeal": meals.meal_cal,
            "carbMeal": meals.meal_carb,
            "protMeal": meals.meal_prot,
            "fatMeal": meals.meal_fat,
        }
        socketio.emit("profile details", user_details)

def emit_all_user_weights(user_email, sid):
    weights = []
    for user_weight in db.session.query(models.Weight).filter_by(email = user_email).all():
        weights.append(user_weight.weight)
    socketio.emit('most recent weight', {
        'weight': weights,
        'sid': sid
    })

@socketio.on('new entry')
def on_new_entry(data):
    db.session.add(models.Weight(datetime.datetime.now(), data['weight'], data['email']))
    db.session.commit()
    socketio.emit('not editing', 'User is no longer editing')
    emit_all_user_weights(data['email'], data['sid'])

@socketio.on("new food search")
def on_new_food_search(data):
    food_name = {"food": data["food_search"]}
    food_response = foodsearch(food_name["food"])
    socketio.emit("food response", food_response)

@socketio.on("new user input")
def on_new_user(data):
    date = str(datetime.datetime.now().date())
    measurements = {
        "height": data["height"],
        "weight": data["weight"],
        "age": data["age"],
        "gender": data["gender"],
        "activityLevel": int(data["activityLevel"][0]),
    }
    google_usr = {"name": data["name"], "email": data["email"], "sid": request.sid}
    bmr = bmr_cal(
        measurements["weight"],
        measurements["height"],
        measurements["age"],
        measurements["gender"],
    )
    calories = daily_caloric_need(bmr, measurements["activityLevel"])
    macros = calculate_macro(calories)
    meals = mealplan(calories)
    profile_data = {
        "weight": data["weight"],
        "activityLevel": data["activityLevel"],
        "gainOrLose": data["gainOrLose"],
        "MaxCalories": macros["MaxCalories"],
    }
    # To fetch the recepies from API getting the variable ready
    db.session.add(
        models.Users(
            google_usr["email"],
            google_usr["name"],
            measurements["height"],
            measurements["age"],
            measurements["gender"],
            measurements["activityLevel"],
            date
        )
    )
    db.session.commit()

    db.session.add(models.Macros(
                                bmr,
                                macros["MaxCalories"],
                                macros["MinCalories"],
                                macros["MaxProtein"],
                                macros["MinProtein"],
                                macros["MaxCarbs"],
                                macros["MinCarbs"],
                                macros["MaxFat"],
                                macros["MinFat"],
                                google_usr["email"],
                        )
                    )
    db.session.commit()

    db.session.add(models.Meals(
                                meals["breakfast"],
                                meals["lunch"],
                                meals["dinner"],
                                meals["nutrients"]["calories"],
                                meals["nutrients"]["carbohydrates"],
                                meals["nutrients"]["protein"],
                                meals["nutrients"]["fat"],
                                google_usr["email"],
                        )
                    )
    db.session.commit()

    db.session.add(models.Weight(datetime.datetime.now(), measurements["weight"], google_usr["email"]))
    db.session.commit()

    print(
        "Created db Entry for "
        + google_usr["name"]
        + " with email "
        + google_usr["email"]
    )
    socketio.emit("success login", google_usr)
    socketio.emit("is not logging in", "")
    online_users.append(google_usr)
    get_user_details(google_usr["email"])
    emit_all_user_weights(google_usr['email'], google_usr['sid'])

@socketio.on("google sign in")
def on_google_sign_in(data):
    google_usr = {"name": data["name"], "email": data["email"], "sid": request.sid}
    login_success = True
    for user in online_users:
            if user['email'] == google_usr['email']:
                login_success = False
                logged_usr = user
                print('\nLogin Failed!\nUser with email \'' + google_usr['email'] + '\' is already logged in!')
                res1 = ('Email: \'' + google_usr['email'] + '\' is already logged in!' 
                        + 'If this isn\'t you, please change your password immediately')
                res2 = ('Someone just tried to login as you! If you weren\'t aware of this, please change your password.')
                socketio.emit('failed login', { 'res': res1 }, room = request.sid)
                break
    if login_success:
        if (
            db.session.query(models.Users.id).filter_by(id=google_usr["email"]).scalar()
            is None
        ):
            print("New User: " + google_usr["name"])
            socketio.emit(
                "is logging in", {"res": "User is attempting to login", "sid": request.sid}
            )
            socketio.emit("new form", google_usr)
        else:
            print("Welcome Back! " + google_usr["name"])
            online_users.append(google_usr)
            socketio.emit("success login", google_usr)
            get_user_details(google_usr["email"])
            emit_all_user_weights(google_usr['email'], google_usr['sid'])

@socketio.on("google sign out")
def on_google_sign_out(data):
    for user in online_users:
        if user['sid'] == request.sid:
            online_users.remove(user)
            break
    print('\nUser with SID \'' + request.sid + '\' has successfully signed out')
    socketio.emit('success logout', {
        'sid': request.sid
    })
@socketio.on("connect")
def on_connect():
    print("\nConnected")

@socketio.on("disconnect")
def on_disconnect():
    for user in online_users:
        if user['sid'] == request.sid:
            online_users.remove(user)
            break
    print("\nDisconnected")

@app.route("/")
def home():
    return flask.render_template("home.html")


@app.route("/profile")
def profile():
    return flask.render_template("profile.html")


@app.route("/foodsearch")
def food_search():
    return flask.render_template("foodSearch.html")

if __name__ == "__main__":
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True,
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )

import requests
import json
from os.path import join, dirname
from dotenv import load_dotenv
import os


DOTENV_PATH = join(dirname(__file__), "sql.env")
load_dotenv(DOTENV_PATH)

spoonacular_key = os.environ['SPOONACULAR_KEY']

def foodsearch(name):
    url1 = "https://api.spoonacular.com/recipes/search?query="
    url2 = "&apiKey={}"
    url3 = url1 + name + url2 
    url = url3.format(spoonacular_key)
    
    response = requests.get(url)
    json_body = response.json()
    image = json_body["results"][0]["image"]
    title = json_body["results"][0]["title"]
    preptime = json_body["results"][0]["readyInMinutes"]
    meal_id = json_body["results"][0]["id"]
    source_URL = json_body["results"][0]["sourceUrl"]
    
    imageid = image.split("-")[-1]
    imageid1 = imageid.split(".")
    imageURL1 = "https://spoonacular.com/recipeImages/" + str(imageid1[0])
    imageURL = imageURL1 + "-480x360." + str(imageid1[1])
    
    recepie_list_URL1 = "https://api.spoonacular.com/recipes/" + str(meal_id)
    recepie_list_URL = recepie_list_URL1 + "/information?includeNutrition=false&apiKey={}".format(spoonacular_key)
    response1 = requests.get(recepie_list_URL)
    json_body1 = response1.json()
    ingredient = json_body1["extendedIngredients"]
    recepie_list =[]
    recepie_len = len(recepie_list)
    
    for item in ingredient:
        key1 = "name"
        if key1 in item:
            recepie_list.append(item['name'])
   
    food_detail={
        'name' : title,
        'image' : image,
        'preptime' : preptime,
        'recepie_list' : recepie_list,
        'imageURL' : imageURL
    }   
           
    return food_detail;
        
        
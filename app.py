import os 
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "meal-ponderer"
app.config["MONGO_URI"] = "mongodb://admin:Mealponderer1@ds131763.mlab.com:31763/meal-ponderer"

mongo = PyMongo(app)

@app.route("/")
def index():
    
    return render_template('index.html')
    
    
@app.route("/recipes")
def get_recipes():
    
    return render_template('recipes.html', recipes=mongo.db.recipe.find())
    
@app.route("/add_recipe")
def add_recipe():
    return render_template("add_recipe.html")

@app.route("/insert_recipe")
def insert_recipe():
    return redirect(url_for("/"))

if __name__ == '__main__':
    app.run(host=os.environ.get("IP"), port=int(os.environ.get('PORT')), debug=True)
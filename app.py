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

@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    doc = {
        "recipe_name":request.form.get('recipe_name'),
        "cuisine":request.form.get('cuisine'),
        "allergen":[request.form.get('special_diet')],
        "recipe_description":request.form.get('recipe_description'),
        "ingredients":[request.form.get('ingredients')],
        "instructions":[request.form.get('instructions')],
        "prep_time":request.form.get('prep_time'),
        "cook_time":request.form.get('cook_time'),
        "serving":request.form.get('serving'),
        "author":request.form.get('author'),
        "recipe_image":request.form.get('recipe_image')
    }
    
    mongo.db.recipe.insert_one(doc)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(host=os.environ.get("IP"), port=int(os.environ.get('PORT')), debug=True)
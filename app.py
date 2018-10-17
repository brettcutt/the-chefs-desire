import os 
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "meal-ponderer"
app.config["MONGO_URI"] = "mongodb://admin:Mealponderer1@ds131763.mlab.com:31763/meal-ponderer"

mongo = PyMongo(app)

cuisines_json = []

with open ("data/cuisine_category.json", "r") as file:
    cuisines_json = json.load(file)

allergens_json = []    
    
with open ("data/allergen_category.json", "r") as file:
    allergens_json = json.load(file)
    

@app.route("/")
def index():
    
    return render_template('index.html')
    
    
@app.route("/recipes")
def recipes():
    
    return render_template('recipes.html', recipes=mongo.db.recipe.find())
    
@app.route("/add_recipe")
def add_recipe():
    return render_template("add_recipe.html", cuisines=mongo.db.cuisines.find(), allergens=mongo.db.allergens.find())

@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    doc = {
        "name":request.form.get('name'),
        "cuisine":(request.form.getlist('cuisine')),
        "allergens":(request.form.getlist('allergens')),
        "description":request.form.get('description'),
        "ingredients":(request.form.getlist('ingredients')),
        "instructions":(request.form.getlist('instructions')),
        "prep_time":request.form.get('prep_time'),
        "cook_time":request.form.get('cook_time'),
        "recipe_yield":request.form.get('recipe_yield'),
        "author":request.form.get('author'),
        "image":request.form.get('image')
    }
    
    mongo.db.recipe.insert_one(doc)
    return redirect(url_for("index"))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe, other_cuisines=cuisines_json, allergens_json=allergens_json)
    
@app.route("/update_recipe/<recipe_id>", methods=['POST'])
def update_recipe(recipe_id):
    
    mongo.db.recipe.update({'_id':ObjectId(recipe_id)},
    {
        "name":request.form.get('name'),
        "cuisine":request.form.getlist('cuisine'),
        "allergens":request.form.getlist('allergens'),
        "description":request.form.get('description'),
        "ingredients":request.form.getlist('ingredients'),
        "instructions":request.form.getlist('instructions'),
        "prep_time":request.form.get('prep_time'),
        "cook_time":request.form.get('cook_time'),
        "recipe_yield":request.form.get('recipe_yield'),
        "author":request.form.get('author'),
        "image":request.form.get('image')
    })

    return redirect(url_for('recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get("IP"), port=int(os.environ.get('PORT')), debug=True)
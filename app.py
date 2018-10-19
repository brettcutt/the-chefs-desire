import os 
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "meal-ponderer"
app.config["MONGO_URI"] = "mongodb://admin:Mealponderer1@ds131763.mlab.com:31763/meal-ponderer" 

mongo = PyMongo(app)

# Data for listing the cuisine categories 
cuisines_json = []

with open ("data/cuisine_category.json", "r") as file:
    cuisines_json = json.load(file)

# Data for listing the allergen categories 

allergens_json = []    
    
with open ("data/allergen_category.json", "r") as file:
    allergens_json = json.load(file)


# Data added and edited in mlabs
def recipe_database():
    data = {
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
    }
    return data
    
# //////////////// Index (render)
@app.route("/")
def index():
    
    return render_template('index.html')

# //////////////// Recipes (render)  
@app.route("/recipes")
def recipes():
    
    return render_template('recipes.html', recipes=mongo.db.recipe.find(), cuisines_json=cuisines_json, allergens_json=allergens_json)

# //////////////// Single_recipes (render)

@app.route('/single_recipe/<recipe_id>')
def single_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})

    return render_template("single_recipe.html", recipe=the_recipe, cuisines_json=cuisines_json, allergens_json=allergens_json)

# //////////////// Found_recipes (render)
@app.route("/find_ingredient", methods=['POST'])
def find_ingredient():
    recipe_category = mongo.db.recipe.find({"ingredients": {"$regex":request.form.get("ingredient_category")}})
    return render_template('search_results.html', recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json)

@app.route("/find_cuisine", methods=['POST'])
def find_cuisine():
    recipe_category = mongo.db.recipe.find({"cuisine":request.form.get("cuisine_category")})
    return render_template('search_results.html', recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json)
    
    
@app.route("/find_allergen", methods=['POST'])
def find_allergen():
    recipe_category = mongo.db.recipe.find({"allergens":{"$nin": request.form.getlist("allergen_category")}})
    return render_template('search_results.html', recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json)    
    
    
@app.route("/find_multiple_categories", methods=['POST'])
def find_multiple_categories():
    
    ingredient = request.form.get("find_ingredient")
    cuisine = request.form.get("find_cuisine")
    allergens = request.form.getlist("find_allergen")
    
    if cuisine == "" and not ingredient:
        recipe_category = mongo.db.recipe.find({"allergens":{"$nin": allergens}})
    
    elif cuisine == "" and not allergens:
        recipe_category = mongo.db.recipe.find({"ingredients": {"$regex":ingredient}})
        
    elif not ingredient and not allergens:
        recipe_category = mongo.db.recipe.find({"cuisine":cuisine})
                                                         
    elif not ingredient and cuisine and allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"cuisine":cuisine},
                                                         {"allergens":{"$nin": allergens}}  ]})
        
    elif ingredient and cuisine == "" and allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"allergens":{"$nin": allergens}},
                                                         {"ingredients":{"$regex":ingredient}}  ]})
                                                         
    elif ingredient and cuisine and not allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"cuisine":cuisine},
                                                         {"ingredients":{"$regex":ingredient}}  ]})
                                                         
    elif ingredient and cuisine and allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"cuisine":cuisine},
                                                         {"allergens":{"$nin": allergens}},
                                                         {"ingredients":{"$regex":ingredient}}  ]})
    print(recipe_category.count())
    recipe_count = recipe_category.count()
    return render_template('search_results.html', recipe_category=recipe_category, recipe_count=recipe_count, cuisines_json=cuisines_json, allergens_json=allergens_json)
  
    
# //////////////// add recipe(render) and insert recipe(redirect)
# Add (render)
@app.route("/add_recipe")
def add_recipe():
    return render_template("add_recipe.html", cuisines=mongo.db.cuisines.find(), allergens=mongo.db.allergens.find())

#Insert (redirect)
@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    doc = recipe_database()
    
    mongo.db.recipe.insert_one(doc)
    return redirect(url_for("recipes"))

# //////////////// Edit recipe and Update recipe
# Edit (render)
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe, cuisines_json=cuisines_json, allergens_json=allergens_json)

# Update (redirect)
@app.route("/update_recipe/<recipe_id>", methods=['POST'])
def update_recipe(recipe_id):
    
    mongo.db.recipe.update({'_id':ObjectId(recipe_id)}, recipe_database())

    return redirect(url_for('recipes'))
    
    
# //////////////// Delete recipe
# Delete (redirect)
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    
    mongo.db.recipe.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('recipes'))



if __name__ == '__main__':
    app.run(host=os.environ.get("IP"), port=int(os.environ.get('PORT')), debug=True)
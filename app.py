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
def recipes():
    
    return render_template('recipes.html', recipes=mongo.db.recipe.find())
    
@app.route("/add_recipe")
def add_recipe():
    return render_template("add_recipe.html")

@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    doc = {
        "name":request.form.get('name'),
        "cuisine":request.form.get('cuisine'),
        "allergens":(request.form.getlist('allergens')),
        "description":request.form.get('description'),
        "ingredients":(request.form.getlist('ingredients')
        ),
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
    return render_template('edit_recipe.html', recipe=the_recipe)
    
@app.route("/update_recipe/<recipe_id>", methods=['POST'])
def update_recipe(recipe_id):
    
    if request.form('ingredients') != "":
        ingredients = request.form.getlist('ingredients')
        mongo.db.recipe.update({'_id':ObjectId(recipe_id)},
        {
            "name":request.form.get('name'),
            "cuisine":request.form.get('cuisine'),
            "allergens":request.form.getlist('allergens'),
            "description":request.form.get('description'),
            "ingredients":ingredients,
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
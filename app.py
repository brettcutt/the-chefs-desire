import os 
import json
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
app = Flask(__name__)

app.secret_key = os.urandom(24)

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
        "image":request.form.get('image'),
        "username": session['user']
    }
    return data
    
def registration_form():
    data = {
        "first_name":request.form.get('register-first-name'),
        "last_name":request.form.get('register-last-name'),
        "username":request.form.get('register-username'),
        "email":request.form.get('register-email'),
        "password":request.form.get('register-password')
    }
    return data
    
# //////////////// INDEX (render)

@app.route("/")
def index():
    
    return render_template('index.html')
    
# //////////////// SIGN IN
@app.route('/signin', methods=['POST'])
def signin():
    
    if 'flash-message2' in session:
        session.pop('flash-message2')
        
    username = request.form.get('signin_username')
    password = request.form.get('signin_password')
    
    try:
        user_doc_username = mongo.db.user_details.find_one({'username':username}, {'username'})
        user_doc_password = mongo.db.user_details.find_one({'username':username}, {'password'})
        for key, value in user_doc_password.items():
        
            if key != "_id":
                stored_password = value
                if password == stored_password:
                    session['user'] = username
        
                    print("user found")
                    return redirect(url_for('my_recipes', username=username))
                    
            else:
                session['flash-message1'] = 1
                test = session['flash-message1']
                print(test)
                flash("Incorrect username or password")
                return redirect(url_for('index'))
    except:
        print("not found")
        return redirect(url_for('index'))
    
# //////////////// LOGOUT

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))

# //////////////// REGISTER
@app.route('/register', methods=['POST'])
def register():
    
    if 'flash-message1' in session:
        session.pop('flash-message1')
    
       
    requested_username = request.form.get("register-username")
    new_password = request.form.get("register-password")
    comfirm_password = request.form.get("comfirm-password")
    
    if comfirm_password == new_password:
        try:
            existing_user = mongo.db.user_details.find_one({'username':requested_username}, {"username"})
            print(existing_user)
            if existing_user == None:
                mongo.db.user_details.insert_one(registration_form())
                username = requested_username
                session['user'] = username
            
                return redirect(url_for('my_recipes', username=username))
            else:
                session['flash-message2'] = 1
                flash("Username already exists")
                print("user name already exists")
                return redirect(request.referrer)
            
        except:
            
            return render_template('index.html')
    else:
        session['flash-message2'] = 2
        flash("Passwords are not the same")
        print("passwords did not match")
        return render_template('index.html',)
        



# //////////////// MY RECIPES
@app.route('/my_recipes/<username>')
def my_recipes(username):
    user = mongo.db.user_details.find_one({"username":username})
    print(session['user'])
    user_recipes = mongo.db.recipe.find({"username":session['user']})
    
    
    return render_template('my_recipes.html', user=user, user_recipes=user_recipes, cuisines_json=cuisines_json, allergens_json=allergens_json)


# //////////////// RECIPES (render) 

@app.route("/recipes")
def recipes():
    
    return render_template('recipes.html', recipes=mongo.db.recipe.find(), cuisines_json=cuisines_json, allergens_json=allergens_json)


# //////////////// SINGLE SEARCHED RECIPE (render)

# UPDATE THE RECIPE VIEWS
@app.route('/update_view_count/<recipe_id>')
def update_view_count(recipe_id):
    recipe_views = mongo.db.recipe.find_one({'_id':ObjectId(recipe_id)}, {"views"})
    
    count = []       
    
    for key, value in recipe_views.items():
        if key !="_id":
            count = value
    if not count:
        mongo.db.recipe.update_one({'_id':ObjectId(recipe_id)},{"$set":{"views": 1 }}, upsert = True)
    elif count >= 0:
        mongo.db.recipe.update({'_id':ObjectId(recipe_id)},{"$set": {"views": count + 1 }})
    
    
    return redirect(url_for('single_recipe', recipe_id=recipe_id ))
    
# SINGLE RECIPE
@app.route('/single_recipe/<recipe_id>')
def single_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    creator_username = ""
    if 'user' in session:
        creator_username = session['user']
    return render_template("single_recipe.html", recipe=the_recipe, cuisines_json=cuisines_json, allergens_json=allergens_json, creator_username=creator_username)
    
    
# UPDATE LIKES
@app.route('/update_like/<recipe_id>')
def update_like(recipe_id):
    
    recipe_likes = mongo.db.recipe.find_one({'_id':ObjectId(recipe_id)}, {"likes"})
    
    count = []       
    
    for key, value in recipe_likes.items():
        if key !="_id":
            count = value
    if not count:
        mongo.db.recipe.update_one({'_id':ObjectId(recipe_id)},{"$set":{"likes": 1 }}, upsert = True)
    elif count >= 0:
        mongo.db.recipe.update({'_id':ObjectId(recipe_id)},{"$set": {"likes": count + 1 }})
        
    return redirect(url_for('single_recipe', recipe_id=recipe_id ))

# //////////////// SEARCHING RESULT (render)

@app.route("/find_ingredient", methods=['POST'])
def find_ingredient():
    recipe_category = mongo.db.recipe.find({"ingredients": {"$regex":request.form.get("ingredient_category")}})
    recipe_count = recipe_category.count()
    return render_template('search_results.html', recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json, recipe_count=recipe_count)

@app.route("/find_cuisine", methods=['POST'])
def find_cuisine():
    recipe_category = mongo.db.recipe.find({"cuisine":request.form.get("cuisine_category")})
    recipe_count = recipe_category.count()
    return render_template('search_results.html', recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json, recipe_count=recipe_count)
    
    
@app.route("/find_allergen", methods=['POST'])
def find_allergen():
    recipe_category = mongo.db.recipe.find({"allergens":{"$nin": request.form.getlist("allergen_category")}})
    recipe_count = recipe_category.count()
    return render_template('search_results.html', recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json, recipe_count=recipe_count)    
    
    
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
  
    
# //////////////// ADD RECIPE(render) AND INSERT RECIPE(redirect)
# Add (render)
@app.route("/add_recipe")
def add_recipe():
    return render_template("add_recipe.html", cuisines_json=cuisines_json, allergens_json=allergens_json)

#Insert (redirect)
@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    doc = recipe_database()
    
    mongo.db.recipe.insert_one(doc)
    return redirect(url_for("recipes"))

# //////////////// EDIT RECIPE AND UPDATE RECIPE
# Edit (render)
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe, cuisines_json=cuisines_json, allergens_json=allergens_json)

# Update (redirect)
@app.route("/update_recipe/<recipe_id>", methods=['POST'])
def update_recipe(recipe_id):
    
    mongo.db.recipe.update_many({'_id':ObjectId(recipe_id)},{"$set": recipe_database()})

    return redirect(url_for('recipes'))
    
    
# //////////////// DELETE RECIPE
# Delete (redirect)
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    
    mongo.db.recipe.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('recipes'))



if __name__ == '__main__':
    app.run(host=os.environ.get("IP"), port=int(os.environ.get('PORT')), debug=True)
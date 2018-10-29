import os 
import json
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
app = Flask(__name__)

app.secret_key = os.urandom(22)

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
        "password":request.form.get('register-password'),
        "liked_recipes":[]
    }
    return data
    
# FUNCTION 1
def find_value(variable):
    item = ""
    for key, value in variable.items():
        if key !="_id":
            item = value
    return item
    
# FUNCTION 2    
def if_user_in_session():
    username = ""
    if 'user' in session:
        username = session['user']
    return username
    
# /////////////////////////////////////////////////////////////////////////////// INDEX (render)

@app.route("/")
def index():
    recipes = mongo.db.recipe.aggregate([{"$sample": {"size": 5}}])
    return render_template('index.html', recipes=recipes)

# /////////////////////////////////////////////////////////////////////////////// REGISTER
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
            
            if existing_user == None:
                
                if 'flash-message2' in session:
                    session.pop('flash-message2')
                    
                mongo.db.user_details.insert_one(registration_form())
                session['user'] = requested_username
                return redirect(url_for('my_recipes', username=requested_username))
                
            else:
                session['flash-message2'] = 1
                flash("Username already exists")
                return redirect(request.referrer)
            
        except:
            return redirect(request.referrer)
            
    else:
        session['flash-message2'] = 2
        flash("Passwords are not the same")
        return redirect(request.referrer)
        
    
# ////////////////////////////////////////////////////////////////////////////// SIGN IN
@app.route('/signin', methods=['POST'])
def signin():
    
    if 'flash-message2' in session:
        session.pop('flash-message2')
        
    username = request.form.get('signin_username')
    password = request.form.get('signin_password')
    
    try:
        user_doc_username = mongo.db.user_details.find_one({'username':username}, {'username'})
        user_doc_password = mongo.db.user_details.find_one({'username':username}, {'password'})
        
        stored_username = find_value(user_doc_username)# FUNCTION 1
        stored_password = find_value(user_doc_password)# FUNCTION 1
        if password == stored_password and username == stored_username:
            if 'flash-message1' in session:
                session.pop('flash-message1')
            session['user'] = username
            return redirect(url_for('my_recipes', username=username))
                
        else:
            session['flash-message1'] = 1
            flash("Incorrect username or password")
            return redirect(request.referrer)
            
    except:
        session['flash-message1'] = 1
        flash("An error occured")
        return redirect(request.referrer)
    
# /////////////////////////////////////////////////////////////////////////////// LOGOUT

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))

# ////////////////////////////////////////////////////////////////////////////// RECIPES (render) 

@app.route("/recipes")
def recipes():
    most_popular_recipes=mongo.db.recipe.find( { "$query": {}, "$orderby": { "likes" : -1 } } ).limit(4)
    most_viewed_recipes=mongo.db.recipe.find( { "$query": {}, "$orderby": { "views" : -1 } } ).limit(4)
    all_recipes=mongo.db.recipe.find( { "$query": {}, "$orderby": { "name" : 1 } } ).limit(4)
    
    return render_template('recipes.html',all_recipes=all_recipes, most_viewed_recipes=most_viewed_recipes, most_popular_recipes=most_popular_recipes, cuisines_json=cuisines_json, allergens_json=allergens_json)


# ////////////////////////////////////////////////////////////////////////////// MY RECIPES( USERS PERSONALLY ADDED RECIPES)
@app.route('/my_recipes/<username>')
def my_recipes(username):
    
    user = mongo.db.user_details.find_one({"username":username})
    user_recipes = mongo.db.recipe.find({"username":session['user']})
    recipe_count = user_recipes.count()
    
    
    return render_template('my_recipes.html', user=user, user_recipes=user_recipes, cuisines_json=cuisines_json, allergens_json=allergens_json, recipe_count=recipe_count)

# ///////////////////////////////////////////////////////////////////////////// UPDATE THE RECIPE VIEWS
@app.route('/update_view_count/<recipe_id>')
def update_view_count(recipe_id):
    recipe_name = mongo.db.recipe.find_one({'_id':ObjectId(recipe_id)}, {"name"})
    recipe_name = find_value(recipe_name)
    
    recipe_views = mongo.db.recipe.find_one({'_id':ObjectId(recipe_id)}, {"views"})
    recipe_author = mongo.db.recipe.find_one({'_id':ObjectId(recipe_id)}, {"username"})
    count = find_value(recipe_views) # FUNCTION 1  
    recipe_author = find_value(recipe_author) # FUNCTION 1
    
    
    if if_user_in_session() != recipe_author and recipe_name not in session:
        session[recipe_name] = True
        
        if not count:
            mongo.db.recipe.update_one({'_id':ObjectId(recipe_id)},{"$set":{"views": 1 }}, upsert = True)
            
        elif count >= 0:
            mongo.db.recipe.update({'_id':ObjectId(recipe_id)},{"$set": {"views": count + 1 }})
    
        return redirect(url_for('single_recipe', recipe_id=recipe_id ))
        
        
    else:
        return redirect(url_for('single_recipe', recipe_id=recipe_id ))
    
# //////////////////////////////////////////////////////////////////////////////  SINGLE RECIPE
@app.route('/single_recipe/<recipe_id>')
def single_recipe(recipe_id):
    
    recipe_name = mongo.db.recipe.find_one({'_id':ObjectId(recipe_id)}, {"name"})
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    username = if_user_in_session() # FUNCTION 2
    
    users_liked_recipes = mongo.db.user_details.find_one({"username": username}, {"liked_recipes"})
    
    
    recipe = find_value(recipe_name)
    
    if if_user_in_session():
        
        if recipe in find_value(users_liked_recipes):
            session['recipe_liked'] = 1

        else:
            session['recipe_liked'] = 0
        return render_template("single_recipe.html", recipe_liked = session['recipe_liked'], recipe=the_recipe, cuisines_json=cuisines_json, allergens_json=allergens_json, username=username)
        
    else:
        session['recipe_liked'] = 2
        return render_template("single_recipe.html", recipe_liked = session['recipe_liked'], recipe=the_recipe, cuisines_json=cuisines_json, allergens_json=allergens_json)

    
# ///////////////////////////////////////////////////////////////////////////// UPDATE LIKES
@app.route('/update_like/<recipe_id>')
def update_like(recipe_id):
    
    try:
        username = if_user_in_session()
        
        recipe_name = mongo.db.recipe.find_one({'_id':ObjectId(recipe_id)}, {"name"})
        recipe_likes = mongo.db.recipe.find_one({'_id':ObjectId(recipe_id)}, {"likes"})
        recipe_author = mongo.db.recipe.find_one({'_id':ObjectId(recipe_id)}, {"username"})
        users_liked_recipes = mongo.db.user_details.find_one({"username": username}, {"liked_recipes"})
        
        recipe_name = find_value(recipe_name)
        recipe_author = find_value(recipe_author)# FUNCTION 1
        recipe_likes = find_value(recipe_likes)  # FUNCTION 1
            
        if username != recipe_author and recipe_name not in find_value(users_liked_recipes): # FUNCTION 2    
        
            mongo.db.user_details.update({'username':username},{"$push":{"liked_recipes": recipe_name }}, upsert = True)
        
            if not recipe_likes:
                mongo.db.recipe.update_one({'_id':ObjectId(recipe_id)},{"$set":{"likes": 1 }}, upsert = True)
                
            elif recipe_likes >= 0:
                mongo.db.recipe.update({'_id':ObjectId(recipe_id)},{"$set": {"likes": recipe_likes + 1 }})
                
            return redirect(url_for('single_recipe', recipe_id=recipe_id ))
            
        else:
            return redirect(url_for('single_recipe', recipe_id=recipe_id ))
    except:
        return redirect(url_for('single_recipe', recipe_id=recipe_id ))

# ////////////////////////////////////////////////////////////////////////////// SEARCHING RESULT (render)

@app.route("/most_popular_recipes")
def most_popular_recipes():
    
    recipe_category = mongo.db.recipe.find( { "$query": {}, "$orderby": { "likes" : -1 } } ).limit(10)
    recipe_count = None
    session["search_title"] = 1
    return render_template('search_results.html', search_title = session["search_title"], recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json, recipe_count=recipe_count)

@app.route("/most_viewed_recipes")
def most_viewed_recipes():
    
    session["search_title"] = 2
    recipe_category = mongo.db.recipe.find( { "$query": {}, "$orderby": { "views" : -1 } } ).limit(10)
    recipe_count = None
    return render_template('search_results.html', search_title = session["search_title"], recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json, recipe_count=recipe_count)
    
@app.route("/all_recipes")
def all_recipes():
    
    session["search_title"] = 3
    recipe_category = mongo.db.recipe.find( { "$query": {}, "$orderby": { "name" : 1 } } )
    recipe_count = None
    return render_template('search_results.html', search_title = session["search_title"], recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json, recipe_count=recipe_count)

@app.route("/find_ingredient", methods=['POST'])
def find_ingredient():
    
    session["search_title"] = 0
    recipe_category = mongo.db.recipe.find({"ingredients": {"$regex": request.form.get("ingredient_category"), "$options": 'i'}})
    recipe_count = recipe_category.count()
    return render_template('search_results.html', recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json, recipe_count=recipe_count)

@app.route("/find_cuisine", methods=['POST'])
def find_cuisine():
    
    session["search_title"] = 0
    recipe_category = mongo.db.recipe.find({"cuisine":request.form.get("cuisine_category").title()})
    recipe_count = recipe_category.count()
    return render_template('search_results.html', recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json, recipe_count=recipe_count)
    
    
@app.route("/find_allergen", methods=['POST'])
def find_allergen():
    
    session["search_title"] = 0
    recipe_category = mongo.db.recipe.find({"allergens":{"$nin": request.form.getlist("allergen_category")}})
    recipe_count = recipe_category.count()
    return render_template('search_results.html', recipe_category=recipe_category, cuisines_json=cuisines_json, allergens_json=allergens_json, recipe_count=recipe_count)    
    
    
@app.route("/find_multiple_categories", methods=['POST'])
def find_multiple_categories():
    
    session["search_title"] = 0
    ingredient = request.form.get("find_ingredient")
    cuisine = request.form.get("find_cuisine").title()
    allergens = request.form.getlist("find_allergen")
    
    if cuisine == "" and not ingredient:
        recipe_category = mongo.db.recipe.find({"allergens":{"$nin": allergens}})
    
    elif cuisine == "" and not allergens:
        recipe_category = mongo.db.recipe.find({"ingredients": {"$regex":ingredient, "$options": 'i'}})
        
    elif not ingredient and not allergens:
        recipe_category = mongo.db.recipe.find({"cuisine":cuisine})
                                                         
    elif not ingredient and cuisine and allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"cuisine":cuisine},
                                                         {"allergens":{"$nin": allergens}}  ]})
        
    elif ingredient and cuisine == "" and allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"allergens":{"$nin": allergens}},
                                                         {"ingredients":{"$regex":ingredient, "$options": 'i'}}  ]})
                                                         
    elif ingredient and cuisine and not allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"cuisine":cuisine},
                                                         {"ingredients":{"$regex":ingredient, "$options": 'i'}}  ]})
                                                         
    elif ingredient and cuisine and allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"cuisine":cuisine},
                                                         {"allergens":{"$nin": allergens}},
                                                         {"ingredients":{"$regex":ingredient, "$options": 'i'}}  ]})
    
    recipe_count = recipe_category.count()
    return render_template('search_results.html', recipe_category=recipe_category, recipe_count=recipe_count, cuisines_json=cuisines_json, allergens_json=allergens_json)
  
    
# /////////////////////////////////////////////////////////////////////////////// ADD RECIPE(render) AND INSERT RECIPE(redirect)
# Add (render)
@app.route("/add_recipe")
def add_recipe():
    return render_template("add_recipe.html", cuisines_json=cuisines_json, allergens_json=allergens_json)

# Insert (redirect)
@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    doc = recipe_database()
    
    username = if_user_in_session() # FUNCTION 2
        
    mongo.db.recipe.insert_one(doc)
    id_num = mongo.db.recipe.find_one({'name':request.form.get('name'), 'username': username})
    
    recipe_id = ""
    for key, value in id_num.items():
        if key == "_id":
            recipe_id = ObjectId(value)
    
    
    return redirect(url_for('single_recipe', recipe_id=recipe_id ))

# /////////////////////////////////////////////////////////////////////////////// EDIT RECIPE AND UPDATE RECIPE
# Edit (render)
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=the_recipe, cuisines_json=cuisines_json, allergens_json=allergens_json)

# Update (redirect)
@app.route("/update_recipe/<recipe_id>", methods=['POST'])
def update_recipe(recipe_id):
    
    username = if_user_in_session() # FUNCTION 2
    
    mongo.db.recipe.update_many({'_id':ObjectId(recipe_id)},{"$set": recipe_database()})
    
    id_num = mongo.db.recipe.find_one({'name':request.form.get('name'), 'username': username})
    
    recipe_id = ""
    for key, value in id_num.items():
        if key == "_id":
            recipe_id = ObjectId(value)
    
    
    return redirect(url_for('single_recipe', recipe_id=recipe_id ))
    
    
# ////////////////////////////////////////////////////////////////////////////// DELETE RECIPE
# Delete (redirect)
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    username = if_user_in_session()
    mongo.db.recipe.remove({'_id':ObjectId(recipe_id)})
    return redirect(url_for('my_recipes', username=username))



if __name__ == '__main__':
    app.run(host=os.environ.get("IP"), port=int(os.environ.get('PORT')), debug=True)
import os
import json
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.debug = False
if app.debug == True:
    import config
    app.secret_key = config.DB_CONFIG['SECRET_KEY']
    app.config["MONGO_DBNAME"] = config.DB_CONFIG['MONGO_DBNAME']
    app.config["MONGO_URI"] = config.DB_CONFIG['MONGO_URI']
else:
    app.secret_key = os.environ.get('SECRET_KEY')
    app.config["MONGO_DBNAME"] = os.environ.get("DBS_NAME")
    app.config["MONGO_URI"] = os.environ.get("MONGODB_URI")
    
mongo = PyMongo(app)


# List of the cuisine categories
cuisines_json = []
with open("data/cuisine_category.json", "r") as file:
    cuisines_json = json.load(file)



# List of the allergen categories
allergens_json = []
with open("data/allergen_category.json", "r") as file:
    allergens_json = json.load(file)
    
"""
 Data added to or edited in mlabs on recipe form submission. 
 Additionally on the add_recipes route, recipe_views and recipe_likes are set 
 to 0. The user in session has their unique username added to the recipe.
 """
def recipe_database():
    data = {
        "name": request.form.get('name'),
        "cuisine": request.form.getlist('cuisine'),
        "allergens": request.form.getlist('allergens'),
        "description": request.form.get('description'),
        "ingredients": request.form.getlist('ingredients'),
        "instructions": request.form.getlist('instructions'),
        "prep_time": request.form.get('prep_time'),
        "cook_time": request.form.get('cook_time'),
        "recipe_yield": request.form.get('recipe_yield'),
        "author": request.form.get('author'),
        "image": request.form.get('image'),
        "username": session['user']
    }
    return data


""" New user details sent to mlabs on user registration form submission.
Every user will have a unique username"""
def registration_form():
    data = {
        "first_name": request.form.get('register_first_name'),
        "last_name": request.form.get('register_last_name'),
        "username": request.form.get('register_username'),
        "email": request.form.get('register_email'),
        "password": request.form.get('register_password'),
        "liked_recipes": []
    }
    return data
"""
FUNCTION 1
A function to return a specific field value after performing a query search"""
def find_value(variable):
    item = ""
    for key, value in variable.items():
        if key != "_id":
            item = value
    return item
    
"""
FUNCTION 2
 A function to say that if the session['user'] variable is in session, 
 username will be what the session variable is. """
def if_user_in_session():
    username = ""
    if 'user' in session:
        username = session['user']
    return username
"""
FUNCTION 3
Removes the session variable if it's in session."""
def pop_flask_message():
    if 'flash-message1' in session:
        return session.pop('flash-message1')
        
"""
FUNCTION 4
returns a list of the current usernames in the mlab database. Used in the 
base.html and combined with jinja and javascript to tell the user on
registration from submission, whether the requested username is taken or not."""
def current_usernames():
    
    items = []
    usernames = mongo.db.user_details.find()
    for item in usernames:
        for key, value in item.items():
            if key == "username":
                items.append(value)  
    return items
    
# /////////////////////////////////////////////////////////////// INDEX (render)
""" Returns 5 random pictures from any recipe added by admin """
@app.route("/")
def index():
    
    usernames = current_usernames() # FUNCTION 4
    recipes = mongo.db.recipe.aggregate([{ "$match": { "username": "admin"} }, {"$sample": {"size": 5}}])
    
    return render_template('index.html', recipes=recipes, usernames=usernames)


# ///////////////////////////////////////////////////////////////////// REGISTER
"""On registration if the passwords don't match or the requested username 
already exists in the database, return the user to the index page. If the 
passwords match and the requested username doesn't exist, than send the 
register form information to the mlab database. Upon a successful 
registration, a session['user'] variable is set to what the requested 
username is."""

@app.route('/register', methods=['POST'])
def register():

    requested_username = request.form.get("register_username")
    new_password = request.form.get("register_password")
    comfirm_password = request.form.get("comfirm_password")

    if comfirm_password == new_password:
        try:
            existing_user = mongo.db.user_details.find_one(
                {'username': requested_username}, {"username"})

            if existing_user is None:

                mongo.db.user_details.insert_one(registration_form())
                session['user'] = requested_username
                return redirect(
                    url_for(
                        'my_recipes',
                        username=requested_username))

            else:
                return redirect(request.referrer)

        except BaseException:
            return redirect(request.referrer)

    else:
        return redirect(request.referrer)


# /////////////////////////////////////////////////////////////////// SIGN IN
""" verifies that the posted username and password from the sign in form
matches the username and password stored in the database.
Upon a successful sign in, a session['user'] variable is set to what the
form username is."""

@app.route('/signin', methods=['POST'])
def signin():

    username = request.form.get('signin_username')
    password = request.form.get('signin_password')

    try:
        user_doc_username = mongo.db.user_details.find_one(
            {'username': username}, {'username'})
        user_doc_password = mongo.db.user_details.find_one(
            {'username': username}, {'password'})

        stored_username = find_value(user_doc_username)  # FUNCTION 1
        stored_password = find_value(user_doc_password)  # FUNCTION 1
        if password == stored_password and username == stored_username:
            if 'flash-message1' in session:
                session.pop('flash-message1')
            session['user'] = username
            return redirect(url_for('my_recipes', username=username))

        else:
            session['flash-message1'] = 1
            flash("Incorrect username or password")
            return redirect(url_for('index'))

    except BaseException:
        session['flash-message1'] = 1
        flash("Incorrect username or password")
        return redirect(url_for('index'))

# ///////////////////////////////////////////////////////////////////// LOGOUT
""" When the logout button is pressed the user session ends and is returned to
the index page"""

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))

# ///////////////////////////////////////////////////////////// RECIPES (render)
""" Returns three different recipe categories. The top 4 most liked recipes,
The top 4 most viewed recipes and the first 4 recipes starting in 
alphabetical order."""

@app.route("/recipes")
def recipes():
    usernames = current_usernames() # FUNCTION 4
    most_popular_recipes = mongo.db.recipe.find(
        {"$query": {}, "$orderby": {"likes": -1}}).limit(4)
    most_viewed_recipes = mongo.db.recipe.find(
        {"$query": {}, "$orderby": {"views": -1}}).limit(4)
    all_recipes = mongo.db.recipe.find(
        {"$query": {}, "$orderby": {"name": 1}}).limit(4)

    pop_flask_message() # FUNCTION 3

    return render_template(
        'recipes.html',
        all_recipes=all_recipes,
        most_viewed_recipes=most_viewed_recipes,
        most_popular_recipes=most_popular_recipes,
        cuisines_json=cuisines_json,
        allergens_json=allergens_json,
        usernames=usernames)


# ////////////////////////////////////////////////////////////////////MY RECIPES
""" Upon registration or login the session['user'] variable is set. If the 
session variable matches the endpoint the user is granted access to their 
account. This is so the user can't change the endpoint to another
username to access that users account. If a user tries to access another account
through the endpoint, that users session ends and returns them to the index
page."""
@app.route('/my_recipes/<username>')
def my_recipes(username):
    pop_flask_message() # FUNCTION 3
    if session['user'] == username:
        user = mongo.db.user_details.find_one({"username": username})
        user_recipes = mongo.db.recipe.find({"username": session['user']})
        recipe_count = user_recipes.count()

        return render_template(
            'my_recipes.html',
            user=user,
            user_recipes=user_recipes,
            cuisines_json=cuisines_json,
            allergens_json=allergens_json,
            recipe_count=recipe_count)

    else:
        session.pop('user')
        return redirect(url_for('index'))
        
# ///////////////////////////////////////////////////// UPDATE THE RECIPE VIEWS
"""Before accessing a recipe the view is routed here, If the user is the one who
added the recipe, the recipe view count won't increase. If a user has previously
accessed the recipe, the view count will increase by one and a session variable 
is set to that recipes name. If the recipe name is in session then the view 
count won't increase"""

@app.route('/update_view_count/<recipe_id>')
def update_view_count(recipe_id):
    recipe_name = mongo.db.recipe.find_one(
        {'_id': ObjectId(recipe_id)}, {"name"})
    recipe_name = find_value(recipe_name) # FUNCTION 1

    recipe_views = mongo.db.recipe.find_one(
        {'_id': ObjectId(recipe_id)}, {"views"})
    recipe_author = mongo.db.recipe.find_one(
        {'_id': ObjectId(recipe_id)}, {"username"})
    count = find_value(recipe_views)  # FUNCTION 1
    recipe_author = find_value(recipe_author)  # FUNCTION 1

    if if_user_in_session() != recipe_author and recipe_name not in session:
    # FUNCTION 2
        session[recipe_name] = True 

        if not count:
            mongo.db.recipe.update_one({'_id': ObjectId(recipe_id)}, {
                                       "$set": {"views": 1}}, upsert=True)

        elif count >= 0:
            mongo.db.recipe.update_one({'_id': ObjectId(recipe_id)}, {
                "$set": {"views": count + 1}})

        return redirect(url_for('single_recipe', recipe_id=recipe_id))

    else:
        return redirect(url_for('single_recipe', recipe_id=recipe_id))


# ///////////////////////////////////////////////////////////////  SINGLE RECIPE
""" A single recipe will be on this view. If a user is in session a few things 
are enabled and disabled with a session variable and referenced with jinja. 
A user in session has the ability to like recipes and a user not in session 
won't be able too. Also if the user in session is also the user who contributed
the recipe, they will have additional 'edit' and 'delete' buttons. """

@app.route('/single_recipe/<recipe_id>')
def single_recipe(recipe_id):
    pop_flask_message() # FUNCTION 3
    usernames = current_usernames() # FUNCTION 4
    recipe_name = mongo.db.recipe.find_one(
        {'_id': ObjectId(recipe_id)}, {"name"})
        
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    username = if_user_in_session()  # FUNCTION 2

    users_liked_recipes = mongo.db.user_details.find_one(
        {"username": username}, {"liked_recipes"})

    recipe = find_value(recipe_name) # FUNCTION 1

    if if_user_in_session():# FUNCTION 2

        if recipe in find_value(users_liked_recipes): # FUNCTION 1
            session['recipe_liked'] = 1

        else:
            session['recipe_liked'] = 0
        return render_template(
            "single_recipe.html",
            recipe_liked=session['recipe_liked'],
            recipe=the_recipe,
            cuisines_json=cuisines_json,
            allergens_json=allergens_json,
            username=username)

    else:
        session['recipe_liked'] = 2
        return render_template(
            "single_recipe.html",
            recipe_liked=session['recipe_liked'],
            recipe=the_recipe,
            cuisines_json=cuisines_json,
            allergens_json=allergens_json,
            usernames=usernames)


# ///////////////////////////////////////////////////////////////UPDATE LIKES
""" If the user presses the heart icon on the recipe page they are redirected to
this route. If the user is also the recipe contributer than the like count won't 
increase. A normal user will add 1 like to the recipe document and add that 
recipes name to their user document. If the user already has the recipe name in
their document, the user will be directed back to the recipe page without
increasing the count."""
@app.route('/update_like/<recipe_id>')
def update_like(recipe_id):

    try:
        username = if_user_in_session()# FUNCTION 2

        recipe_name = mongo.db.recipe.find_one(
            {'_id': ObjectId(recipe_id)}, {"name"})
        recipe_likes = mongo.db.recipe.find_one(
            {'_id': ObjectId(recipe_id)}, {"likes"})
        recipe_author = mongo.db.recipe.find_one(
            {'_id': ObjectId(recipe_id)}, {"username"})
        users_liked_recipes = mongo.db.user_details.find_one(
            {"username": username}, {"liked_recipes"})

        recipe_name = find_value(recipe_name) # FUNCTION 1
        recipe_author = find_value(recipe_author)  # FUNCTION 1
        recipe_likes = find_value(recipe_likes)  # FUNCTION 1

        if username != recipe_author and recipe_name not in find_value(
                users_liked_recipes):  # FUNCTION 1

            mongo.db.user_details.update({'username': username}, {"$push": {
                                         "liked_recipes": recipe_name}},
                                         upsert=True)

            if not recipe_likes:
                mongo.db.recipe.update_one({'_id': ObjectId(recipe_id)}, {
                                           "$set": {"likes": 1}}, upsert=True)

            elif recipe_likes >= 0:
                mongo.db.recipe.update_one({'_id': ObjectId(recipe_id)}, {
                    "$set": {"likes": recipe_likes + 1}})

            return redirect(url_for('single_recipe', recipe_id=recipe_id))

        else:
            return redirect(url_for('single_recipe', recipe_id=recipe_id))
    except BaseException:
        return redirect(url_for('single_recipe', recipe_id=recipe_id))

# //////////////////////////////////////////////////// SEARCHING RESULT (render)
""" Routes triggered on submission of a filled out search model. This finds any 
document matching specific values in the recipe collection."""


""" Returns the top 10 documents with the most recipe likes """
@app.route("/most_popular_recipes")
def most_popular_recipes():
    pop_flask_message() # FUNCTION 3
    usernames = current_usernames() # FUNCTION 4
    recipe_category = mongo.db.recipe.find(
        {"$query": {}, "$orderby": {"likes": -1}}).limit(10)
    recipe_count = None
    session["search_title"] = 1
    return render_template(
        'search_results.html',
        search_title=session["search_title"],
        recipe_category=recipe_category,
        cuisines_json=cuisines_json,
        allergens_json=allergens_json,
        recipe_count=recipe_count,
        usernames=usernames)

""" Returns the top 10 documents with the most recipe views """
@app.route("/most_viewed_recipes")
def most_viewed_recipes():
    pop_flask_message() # FUNCTION 3
    usernames = current_usernames() # FUNCTION 4
    session["search_title"] = 2
    recipe_category = mongo.db.recipe.find(
        {"$query": {}, "$orderby": {"views": -1}}).limit(10)
    recipe_count = None
    return render_template(
        'search_results.html',
        search_title=session["search_title"],
        recipe_category=recipe_category,
        cuisines_json=cuisines_json,
        allergens_json=allergens_json,
        recipe_count=recipe_count,
        usernames=usernames)

""" Returns all documents in alphabetical order. """
@app.route("/all_recipes")
def all_recipes():
    pop_flask_message() # FUNCTION 3
    usernames = current_usernames()# FUNCTION 4
    session["search_title"] = 3
    recipe_category = mongo.db.recipe.find(
        {"$query": {}, "$orderby": {"name": 1}})

    recipe_count = None
    return render_template(
        'search_results.html',
        search_title=session["search_title"],
        recipe_category=recipe_category,
        cuisines_json=cuisines_json,
        allergens_json=allergens_json,
        recipe_count=recipe_count,
        usernames=usernames)

""" Returns any document by a word matching a value inside a recipes ingredients
list. """
@app.route("/find_ingredient", methods=['POST'])
def find_ingredient():
    pop_flask_message() # FUNCTION 3
    usernames = current_usernames()# FUNCTION 4
    session["search_title"] = 0
    recipe_category = mongo.db.recipe.find(
        {"ingredients": {"$regex": request.form.get("ingredient_category"), "$options": 'i'}})
    recipe_count = recipe_category.count()
    return render_template(
        'search_results.html',
        recipe_category=recipe_category,
        cuisines_json=cuisines_json,
        allergens_json=allergens_json,
        recipe_count=recipe_count,
        usernames=usernames)

""" Returns any document by a cuisine selection in the search model """
@app.route("/find_cuisine", methods=['POST'])
def find_cuisine():
    pop_flask_message() # FUNCTION 3
    usernames = current_usernames()# FUNCTION 4
    session["search_title"] = 0
    recipe_category = mongo.db.recipe.find(
        {"cuisine": request.form.get("cuisine_category").title()})
    recipe_count = recipe_category.count()
    return render_template(
        'search_results.html',
        recipe_category=recipe_category,
        cuisines_json=cuisines_json,
        allergens_json=allergens_json,
        recipe_count=recipe_count,
        usernames=usernames)

""" Returns any document not containing the allergen value in the search model 
"""
@app.route("/find_allergen", methods=['POST'])
def find_allergen():
    pop_flask_message() # FUNCTION 3
    usernames = current_usernames()# FUNCTION 4
    session["search_title"] = 0
    recipe_category = mongo.db.recipe.find(
        {"allergens": {"$nin": request.form.getlist("allergen_category")}})
    recipe_count = recipe_category.count()
    return render_template(
        'search_results.html',
        recipe_category=recipe_category,
        cuisines_json=cuisines_json,
        allergens_json=allergens_json,
        recipe_count=recipe_count,
        usernames=usernames)

""" Returns any document by the combination of ingredient, 
cuisine and or allergen values."""
@app.route("/find_multiple_categories", methods=['POST'])
def find_multiple_categories():
    pop_flask_message() # FUNCTION 3
    usernames = current_usernames()# FUNCTION 4
    session["search_title"] = 0
    ingredient = request.form.get("find_ingredient")
    cuisine = request.form.get("find_cuisine").title()
    allergens = request.form.getlist("find_allergen")

    if cuisine == "" and not ingredient:
        recipe_category = mongo.db.recipe.find(
            {"allergens": {"$nin": allergens}})

    elif cuisine == "" and not allergens:
        recipe_category = mongo.db.recipe.find(
            {"ingredients": {"$regex": ingredient, "$options": 'i'}})

    elif not ingredient and not allergens:
        recipe_category = mongo.db.recipe.find({"cuisine": cuisine})

    elif not ingredient and cuisine and allergens:
        recipe_category = mongo.db.recipe.find(
            {"$and": [{"cuisine": cuisine}, {"allergens": {"$nin": allergens}}]})

    elif ingredient and cuisine == "" and allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"allergens": {"$nin": allergens}}, {
                                               "ingredients": {"$regex": ingredient, "$options": 'i'}}]})

    elif ingredient and cuisine and not allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"cuisine": cuisine}, {
                                               "ingredients": {"$regex": ingredient, "$options": 'i'}}]})

    elif ingredient and cuisine and allergens:
        recipe_category = mongo.db.recipe.find({"$and": [{"cuisine": cuisine},
                                                         {"allergens": {"$nin": allergens}},
                                                         {"ingredients": {"$regex": ingredient, "$options": 'i'}}]})

    recipe_count = recipe_category.count()
    return render_template(
        'search_results.html',
        recipe_category=recipe_category,
        recipe_count=recipe_count,
        cuisines_json=cuisines_json,
        allergens_json=allergens_json,
        usernames=usernames)


# ////////////////////////////// ADD RECIPE(render) AND INSERT RECIPE(redirect)
""" The route to the add recipes page"""
@app.route("/add_recipe")
def add_recipe():
    return render_template(
        "add_recipe.html",
        cuisines_json=cuisines_json,
        allergens_json=allergens_json)

# Insert (redirect)
""" Upon submmission of a form in the add recipes page, the form field 
infomation is inserted into a document and into the recipe collection."""

@app.route("/insert_recipe", methods=['POST'])
def insert_recipe():
    doc = recipe_database()

    username = if_user_in_session()  # FUNCTION 2

    mongo.db.recipe.insert_one(doc)
    id_num = mongo.db.recipe.find_one(
        {'name': request.form.get('name'), 'username': username})

    recipe_id = ""
    for key, value in id_num.items():
        if key == "_id":
            recipe_id = ObjectId(value)
    mongo.db.recipe.update_one({'_id': ObjectId(recipe_id)}, {
        "$set": {"views": 0}}, upsert=True)
    mongo.db.recipe.update_one({'_id': ObjectId(recipe_id)}, {
        "$set": {"likes": 0}}, upsert=True)
    return redirect(url_for('single_recipe', recipe_id=recipe_id))

# /////////////////////////////////////////////// EDIT RECIPE AND UPDATE RECIPE
""" The route to the edit recipes page. It gets the recipe by the id to 
display all that recipes information in the form fields."""

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):

    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template(
        'edit_recipe.html',
        recipe=the_recipe,
        cuisines_json=cuisines_json,
        allergens_json=allergens_json)

# Update (redirect)
""" Upon submmission of a form in the edit recipes page, the document
being edited is updated with the form field values. I also added that the recipe
can only be updated if the user in session is 'admin' or the session user 
matches the name of the user who contributed the recipe"""

@app.route("/update_recipe/<recipe_id>", methods=['POST'])
def update_recipe(recipe_id):

    username = if_user_in_session()  # FUNCTION 2

    author = mongo.db.recipe.find_one({'_id': ObjectId(recipe_id)})
    contributer = ""
    for key, value in author.items():
        if key == "username":
            contributer = value

    if username == contributer or username == "admin":
        mongo.db.recipe.update_many({'_id': ObjectId(recipe_id)}, {
                                    "$set": recipe_database()})

        id_num = mongo.db.recipe.find_one(
            {'name': request.form.get('name'), 'username': username})

        recipe_id = ""
        for key, value in id_num.items():
            if key == "_id":
                recipe_id = ObjectId(value)

        return redirect(url_for('single_recipe', recipe_id=recipe_id))
    else:
        session.pop('user')
        return redirect(url_for('index'))

# ///////////////////////////////////////////////////////// DELETE RECIPE
""" Upon a click of the delete comfirmation button, that recipes document is
removed from the database. I also added that the recipe
can only be deleted if the user in session is admin or the session user 
matches the name of the user who contributed the recipe"""

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    username = if_user_in_session() # FUNCTION 2

    author = mongo.db.recipe.find_one({'_id': ObjectId(recipe_id)})
    contributer = ""
    for key, value in author.items():
        if key == "username":
            contributer = value

    if username == contributer or username == "admin":

        mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
        return redirect(url_for('my_recipes', username=username))
        
    else:
        session.pop('user')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP"),
        port=int(
            os.environ.get('PORT')),
        debug=False)

# The Chefs Desire
This is the fourth milestone project for the Full-Stack software development course through Code Institute. I decided to base my project on the example 
brief given to the students of this course, which is to create a cookbook. The module before the project focused on creating databases following CRUD 
operations in MySql and NoSql. I decided to use Mongodb(NoSql) as it had a more flexible and rich approach to storing and accessing key/ values.

The project had to allow users to be able to:
- store, access, edit and delete their own recipes. 
- View other users recipes
- search for recipes base on various criteria.
- Show a complete detailed view of each recipe.

It is optional to have user regitration.


# Table of Contents

1. [UX](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#ux)
   - [Strategy](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#strategy)
   - [Existing Features](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#existing-features)
       - [User registration and account](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#user-registration-and-account)
       - [Header and Footer](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#header-and-footer)
       - [index](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#index)
       - [Recipes](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#recipes)
       - [Single Recipe](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#single-recipe)
       - [My recipes](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#my-recipes)
       - [Add and Edit Recipe](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#add-and-edit-recipe)
       - [Delete Recipe](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#delete-recipe)
    - [Features left to implement](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#features-left-to-implement)
    - [Wire Frames](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#wire-frames)
2. [Technologies, Libraries and Languages](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#technologies-libraries-and-languages)
   - [Manual Testing](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#manual-testing)
   - [Automated Tests](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#automated-tests)
   - [Testing Issues](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#testing-issues)
   - [Validation](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#validation)
3. [Testing](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#testing)
4. [Deployment](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#deployment)
5. [Running the code locally](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#running-the-code-locally)
6. [Credits](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#credits)
   - [Bits and pieces of code that helped me along the way](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#bits-and-pieces-of-code-that-helped-me-along-the-way)
   - [Information for the recipes](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#information-for-the-recipes)
   - [media](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#media)
   - [Acknowledgements](https://github.com/brettcutt/the-chefs-desire/blob/master/README.md#acknowledgements)
___

## UX
### Strategy
- As a user I would expect to be able to view various recipes based on different categories e.g.(cuisine, allergens, ingredient) 
- As a user I would want to be able to create an account with my own unique username and password.
- As an account holder I would be expect to have a personal page where they can add their own recipes, see the recipes, edit the recipes and delete them. 
- As a user I would expect a recipe to display at least a picture, its ingredients and instructions of how to make the recipe. 
- As a user I would like to judge the quality of a recipe on other users decisions.

### Existing Features
##### User registration and account
- A user can create an account and have their own unique username. This username will be used to log in and identify a recipe belonging to that user.

##### Header and Footer
- The site name is displayed in the upper left hand corner of the page as a clickable logo that redirects to the home page.
- Navigation buttons are at the upper right hand corner of the page. 
- On mobile the nav menu disappears and a burger menu is there in its place. When clicked the burger icon opens a menu with the navigation buttons.
- A GitHub icon in the footer redirects to my GitHub repository.

##### Index
- This is the home page featuring a larger title for the whole site.
- There are appearing and disappearing images based on 5 random recipes images in the database.
- A tagline is under the image to give knowledge to the user that they can create an account.
- Under the tagline are two buttons. One to open a registration form and the other to redirect to more recipes.
If an account holder is in session, the register button won't be on the home screen.

##### Recipes
- There is a search bar that allows the user to define a search by cuisine, allergen, ingredient or by multiple options. This redirects to a new page on submission of the search results.
- This features three sub category sections with four different recipes for those categories. Each section has a 'see all' button to be directed to a page that 
has more of that type of sub category.

##### Single Recipe
- The main page for a single recipe displays the:
  - recipe name
  - authors name
  - prep time, cook time and servings
  - description
  - ingredients
  - instructions
  - allergens and cuisines
  - image
  - views and likes
- The like button is clickable for account holders, and for non account holders a message displays stating they need to register to like the recipe. The message also contains
a register button and a close button.
- An account holder which is also the creator of the recipe, will have additional delete and edit buttons.

##### My Recipes 
- This section is for an account holder, where the user can add a recipe to contribute to the site.
- Any created recipes will be displayed on this page.

##### Add and Edit Recipe
- These pages have the form inputs for the information of the recipe the user is adding or editing.
- When adding a recipe, the users unique username is also added to the recipe document and this is how these recipes are accessed in the 'my recipes' page.

##### Delete Recipe
- A button is displayed on a recipe page if the user is also the page contributer. This will delete the recipe from the database collection.

### Features left to implement
- Recipe reviews, so a user can leave a comment at the bottom of the recipe page.

### Wire Frames
- Click [here](https://github.com/brettcutt/the-chefs-desire/blob/master/static/images/wireframes/wireframes.md) for wireframe images.
___

## Technologies, Libraries and Languages
- **Python**
  - Implement the logic, functionality and responses of the project.
  - https://www.python.org/
 
- **MongoDB**
  - A noSql database program for storing all recipe and user values.
  - https://www.mongodb.com/

- **Pymongo**
  - The PyMongo distribution contains tools for interacting with MongoDB database from Python
  - https://api.mongodb.com/python/current/

- **Jquery was used on the following:**
  - The changing image on the index page. 
  - pop up registration, sign in, like message, mobile nav menu and the search form.
  - Adding and removing inputs in the add and edit pages.
  - https://jquery.com/
  
- **BootStrap**
  - Made the app responsive on all devices e.g. using "col-xs-12".
  - http://getbootstrap.com/

- **jinja** 
  - Implement python code into html 5

- **Flask**
  - Redirecting and rendering of page route through python
  - http://flask.pocoo.org/
  - 
- **HTML 5**
  - positioning and format of html elements.

- **CSS 3**
  - Styling the HTML elements.
  
- **Font Awesome**
  - the GitHub icon on the footer.
  - https://fontawesome.com/icons/github?style=brands
  - https://fontawesome.com/license
  
- **Google Font**
  - For the font styles "Josefin Slab" and "Indie Flower"
  - https://fonts.google.com/
___

### Testing
#### Manual testing
- Click [here](https://github.com/brettcutt/the-chefs-desire/blob/master/tests/testing.md) for manual testing 

#### Automated Tests   
- Click [here](https://github.com/brettcutt/the-chefs-desire/blob/master/test_basic.py) for automated testing

#### Testing Issues
- **jinja for loop problem:**
I had the cuisine categories stored in mlab to access through a 'for loop' within another 'for loop' which accessed my 
recipes. All the select input fields were expected to show the cuisine categories, except only the first select input
field showed all the categories and the one following it didn't. To fix this I
added the cuisine category as a json format to a separate py file.

- **Finding multiple categories:**
   - In my 'find_multiple_categories' view I originally had something like the following example, so users could do an advanced search

 ```
 mongo.db.recipe.find( {
    "$or" : [
        { "$and" : [ {"allergens":{"$nin": request.form.getlist("find_allergen")}}, {"cuisine":request.form.get("find_cuisine")} ] },
        { "$or" : [ {"allergens":{"$nin": request.form.getlist("find_allergen")}}, {"cuisine":request.form.get("find_cuisine")} ] }
    ]
} )
```

   - After many different approaches and alterations to this code I just couldn't get it to work in a way that searched the different outcomes.
The main problem I think was that the select tag was always giving a value, even if nothing was selected. To fix this, I wrote if else'
statements to cover each outcome of the search possibilities.

- **Broken image link popping user session:**
  - My mentor pointed out a security issue where a user could potentially change the endpoint username to access another users account.
  - My counter was that upon login a user `session['user']` starts based on the login username. If the endpoint doesn't match the `session['user']`
  pop the session.
  - When I added a new recipe with a false image address, this created an error when the picture was loaded and that would cause the user session
  to pop. Every time I signed in to go to the 'my recipes' page and if one of the recipe image addresses was broken , the session would end. If I changed page
  from the 'my recipes' page to another you could clearly see the 'sign in' button appears instead of the 'log out' button.
  - My original solution was to add an `onerror` to all `img` tags and load a default 'missing image' picture. This didn't prevent the session from popping.
  - My next solution was to find a way to verify that the image address link exists. I achieved this by implementing some javascript found from
  https://stackoverflow.com/questions/24577534/javascript-how-to-check-if-a-typed-image-url-really-exists. 
  - The next problem with this code, was it had a sub function within the main function. On the submission of a form with a broken image address, I would
  receive an alert but the process of form submission was too far ahead of the sub function to stop it from sending.
  - To counter this if I added `oninput` on the image `input` to check as the users image address is valid. If it isn', the classname of the input would
  change. Then on form submission a function would check the classname. If `False`, cancel the form.
  - This works pretty well but still with its own issue. Checking the image address takes a second to verify, so its possible to send the form before
  the validation is complete but this the best solution so far.


#### Validation
- **HTML**
  - Checked with W3C validator. Only Jinja related errors due to the validation not programmed to read them. 
- **CSS**
   - Checked with Jigsaw validator and received no errors.
- **Python**
  - Formatted with autopep8 and checked with flake8.  
  `sudo pip install --upgrade autopep8`   
  `autopep8 --in-place --aggressive --aggressive app.py`   
  `sudo pip install flake8`   
   `flake8 app.py`
  
  ___

## Deployment
- **In Heroku**
   - Created a new app and called it `the-chefs-desire`
- **In the terminal command line entered:**
   - `heroku login` Entered username and password.   
   - `git init` to initialise a git repository.
   - `git remote add heroku https://the-chefs-desire.herokuapp.com/` to link the GitHub repository to the Heroku app.
   - `pip3 freeze --local > requirements.txt` Creates a .txt file which tells Heroku what dependencies the project is using.
   - `echo web: python run.py >procfile` Tells Heroku that this project is a web app and that "app.py" is going the run it.
   - `ps:scale web=1`
   
- **In app.py set the app.config variables so Heroku can find them.**
   ```python
   app.secret_key = os.environ.get('SECRET_KEY')
   app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
   app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
   ```
- **In the terminal line entered:**
  
  - `git add`
  - `git commit -m "message"`
  - `git push -u heroku master` pushes the project to Heroku.
 
- **In Heroku:**
   - Go to the project > setting > config vars
   ```
   IP = `0.0.0.0`
   PORT =  `8080`
   SECRET_KEY = |secret key|
   MONGO_DBNAME = |database name|
   MONGO_URI = mongodb://|username|:|password|@ds249233.mlab.com:49233/|database name|
   ```
   - More > restart all dynos

- **Find the code running here:**
   - https://the-chefs-desire.herokuapp.com/

## Running the code locally
- **In the terminal command line enter:**
   - `git clone https://github.com/brettcutt/the-chef-desire.git`
   - `sudo pip3 install flask`
   - `sudo pip3 install pymongo`
   - `sudo pip3 install flask_pymongo`
- **Set up a database in mlabs**
   - https://mlab.com/welcome/
   - Create an account.
   - Create a new deployment (database). The name of the database will be the name entered into the `|database name|` in steps below.
   - Create a new user. Set a username and password for that database.
   - Take note of the MongoDB URI after creating a user e.g. `mongodb://|yourusername|:|yourpassword|@ds249233.mlab.com:49233/|yourdatabasename|`. This will be entered in steps below.
   - Create 4 collections called `'recipe', 'allergens', 'cuisines' `and` 'user_details'`.
   - In `the-meal-ponderer/data` directory copy the data from `allergen_category.json` and `allergen_category.json` and paste it into the `allergens` and `cuisines` collection as a document.
- **In the project folder create a** `config.py` **file**.
   - In the terminal line enter `echo 'config.py' > gitignore` to hide the `config.py` file.
   - In the config.py file enter the following: 
    ```python
     DB_CONFIG = {   
        ' MONGO_DBNAME ':'|database name|',
        ' MONGO_URI ': 'mongodb://|username|:|password|@ds249233.mlab.com:49233/|database name|'
        ' SECRET_KEY ': '|secret key|'
    }
    ```
    - **In app.py, set the app.config variables to the variables set in the config.py file**
    ```python
    import config
    app.config["MONGO_DBNAME"] = config.DB_CONFIG['MONGO_DBNAME']
    app.config["MONGO_URI"] = config.DB_CONFIG['MONGO_URI']
    app.secret_key = config.DB_CONFIG['SECRET_KEY']
    ```
- **In the terminal line enter:**
  - `python3 app.py` to run the app.
___

### Credits
#### Pages that helped along the way.
   
- Mongo how to order a collection by a specific field.
   - https://docs.mongodb.com/manual/reference/operator/meta/orderby/

- Mongo Finding an ingredient by upper or lower case .
   - https://stackoverflow.com/questions/10700921/case-insensitive-search-with-in

- Mongo Return documents without a specific value.
   - https://docs.mongodb.com/manual/reference/operator/query/nin/
   
- mongo multiple pymongo queries: find with "and" and "or"  .
   - https://stackoverflow.com/questions/40388657/query-mongodb-with-and-and-multiple-or

- Javascript validate that at least one field is filled out in the advanced search
   - https://www.sitepoint.com/community/t/validation-check-to-make-sure-at-least-one-field-is-filled-out/2329
  
Javascript validation of the image address
    - https://stackoverflow.com/questions/24577534/javascript-how-to-check-if-a-typed-image-url-really-exists
    - written by eithed
 
- jquery function to add input fields.   
   - https://www.youtube.com/watch?v=jSSRMC0F6u8
   
- Jquery disable scrolling when the search form appears.
   - https://stackoverflow.com/questions/3656592/how-to-programmatically-disable-page-scrolling-with-jquery

- Jquery scroll to top.
   - https://stackoverflow.com/questions/5580350/jquery-cross-browser-scroll-to-top-with-animation
   
- Flask request.referrer.
   - https://stackoverflow.com/questions/45040365/flask-redirect-to-page-then-come-back
   
- markdown commands.
  - https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

- markdown creating a table of content in the README.md.
   - https://www.setcorrect.com/portfolio/work11/

- python Finding my local datetime to implement added recipe date.
   - https://stackoverflow.com/questions/25837452/python-get-current-time-in-right-timezone
   

#### Information for the recipes
- the recipe: name, cuisine, ingredients, instructions and images came from `https://www.themealdb.com/api.php`
- The recipe: prep time, cook time and servings came from external recipe sites.  
- the recipe descriptions were googled by their recipe name and obtained from wikipedia.
- I used the free test api key from `https://www.themealdb.com/api.php` and no attribution was stated.
- **All the information collect is for learning purposes.**


#### media
- background picture
   - https://pxhere.com/en/photo/1369811
- Missing Picture
   - https://commons.wikimedia.org/wiki/File:Missing-image-232x150.png

- Font Awesome
   - GitHub icon
   - plus and remove button icons
   - timer and cutlery icons

### Acknowledgements
- My mentor Mossa Hassan
   - Credit is due to my mentor when it came to the unit testing. There were alot emails trying to get particular tests to pass.
  The following code came from Moosa and was implemented in basic_test.py.
        ```
        content_type='multipart/form-data'
        data=dict( "list" )
        register_username='m' + str(random.randint(1,1000))
        print(dir(response))
        ```
    


# The Chefs Desire
- This is the fourth milestone project for the Full-Stack software development course through Code Institute. I decided to base my project on the example brief given to the
the students of this course, which is to create a cookbook. The module before the project focused on creating databases following CRUD operations in MySql and NoSql. I decided
to use Mongodb(NoSql) as it had a more flexible and rich approach to storing and accessing key/ values.
___
## UX
### Strategy
- As a user I would expect to be able to view various recipes based on different categories e.g.(cuisine, allergens, ingredient) 
- As a user I would want to be able to create an account with my own username and password.
- As an account holder I would be expect to have a personal page where they can add my own recipes, see the recipes and delete or edit them. 
- As a user I would expect a recipe to display atleast a picture, its ingredients and instructions of how to make the recipe. 
- As a user I would like to judge the quality of a recipe on other users decisions.


### Scope
#### Features
##### User registration and account
- A user can create an account and have their own unique username. This username will be used to identify a recipe belonging to that user.

##### Header and Footer
- The site name is displayed in the upper left hand corner of the page as a clickable logo that redirects to the home page.
- Navigation buttons are at the upper right hand corner of the page. 
- On mobile the nav menu disappears and a burger menu is there in its place. When clicked the burger icon opens a menu with the navigation buttons.
- A GitHub icon in the footer redirects to my GitHub repository.

##### Index
- This is the home page featuring a larger title to the whole site.
- There are appearing and disappearing images based on 5 random recipes images in the database.
- A tagline is under the image to give knowledge to the user that they can create an account.
- Under the tagline are two buttons. One to open a registration form and the other to redirect to more recipes.
If an account holder is in session, the register button won't be on the home screen.

##### Recipes
- There is a search bar that allows the user to define a search by cuisine, allergen, ingredient or by multiple options. This redirect to a new page with the
search results.
- This features three sub category sections with four different recipes in each. Each section has a 'see all' button to by directed to a page that 
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
-An account holder which is also the creator of the recipe will have additional delete and edit buttons.

##### My Recipes 
- This section is for an account holder, where the user can add a recipes to contribute to the site.
- Any created recipes will be displayed on this view.

##### Add and Edit Recipe
- These pages have the form inputs for the information of the recipe the user is adding or editing.
- When adding a recipe, the users unique username is also added to the recipe document and this is how these recipes are accessed in the my recipes page.

##### Delete Recipe
- A button displayed on the users recipe to delete it from the collection.
___
### Technologies, Libraries and Languages
- Python
  - Implement the logic, functionality and responses of the project.
  - https://www.python.org/
 
- MongoDB
  - A noSql database program for storing all recipe and user values.
  - https://www.mongodb.com/

- Pymongo
- The PyMongo distribution contains tools for interacting with MongoDB database from Python
- https://api.mongodb.com/python/current/

- Jquery was used on the following:
  - The changing image on the index page. 
  - pop up registration, sign in, like message, mobile nav menu and search form.
  - Adding and removing inputs in the add and edit pages.
  - https://jquery.com/
  
- BootStrap
  - Made the app responsive on all devices e.g. using "col-xs-12".
  - http://getbootstrap.com/

- jinja 
  - Implement python code into html 5

- Flask
  - Redirecting and rendering of page views through python
  - http://flask.pocoo.org/
  - 
- HTML 5
  - positioning and format of html elements.

- CSS 3
  - Style the HTML elements.
  
- Font Awesome
  - the GitHub icon on the footer.
  - https://fontawesome.com/icons/github?style=brands
  - https://fontawesome.com/license
  
- Google Font
  - For the font styles "Josefin Slab" and "Indie Flower"
  - https://fonts.google.com/
___

### Testing
##### Manual testing
- Click [here](https://github.com/brettcutt/the-chefs-desire/blob/master/tests/testing.md) for manual testing 

##### Automated Tests   
- Click [here](https://github.com/brettcutt/the-chefs-desire/blob/master/test_basic.py) for automated testing

#### Testing Issues
- jinja for loop problem:   
I had the cuisine categories stored in mlab to access through a for loop within another forloop which accessed my 
recipes. All the select input fields were expected to show the cuisine categories, except only the first select input
field showed all the categories and the one following it didn't. To fix this I
added the cuisine category as a json format to a separate py file.

- Finding multiple categories
   - In my find_multiple_categories view I originally had something like the following so users could do an advanced search

  - mongo.db.recipe.find( {
    "$or" : [
        { "$and" : [ {"allergens":{"$nin": request.form.getlist("find_allergen")}}, {"cuisine":request.form.get("find_cuisine")} ] },
        { "$or" : [ {"allergens":{"$nin": request.form.getlist("find_allergen")}}, {"cuisine":request.form.get("find_cuisine")} ] }
    ]
} )

   - After many different approaches and alterations to this code I just couldn't get it to work in a way that searched the different outcomes.
The main problem I think was that the select tag is always giving a value, even if nothing is selected. To fix this I wrote if else
statements to cover each outcome of the search possibilities.

#### Validation
- HTML
  - Checked with W3C validator. Only Jinja related errors due to the validation not programmed to read them. 
- css
   - Checked with Jigsaw validator and received no errors.
- python
  - Formatted with autopep8 and checked with flake8. I still have lines that are too long but left them that way for my own readibility at the moment.
  - sudo pip install --upgrade autopep8
  - autopep8 --in-place --aggressive --aggressive app.py
  - sudo pip install flake8
  - flake8 app.py
  
  ___

### Deployment
- In heroku
   - Created a new app
- In the terminal command line entered:
   - `heroku login` Entered username and password.   
   - `git init` to Intilised a git repository.
   - `git remote add heroku https://the-chefs-desire.herokuapp.com/` to link the GitHub repository to the Heroku app.
   - `pip3 freeze --local > requirements.txt` Creates a .txt file which tells Heroku what dependencies the project is using.
   - `echo web: python run.py >procfile` Tells Heroku that this project is a web app and that "app.py" is going the run it.
   - `ps:scale web=1`
   
- In app.py set the app.config variables so heroku can find them.
   ```
   app.secret_key = os.environ.get('SECRET_KEY')
   app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
   app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
   ```
- In the terminal line entered:
  
  - `git add`
  - `git commit -m "message"`
  - `git push -u heroku master` pushes the project to Heroku.
 
- In heroku:
   - Go to the project > setting > config vars
   ```
   IP = `0.0.0.0`
   PORT =  `8080`
   SECRET_KEY = |secret key|
   MONGO_DBNAME = |database name|
   MONGO_URI = mongodb://|username|:|password|@ds249233.mlab.com:49233/|database name|
   ```
   - More > restart all dynos

- Find the code running here:
   - https://the-chefs-desire.herokuapp.com/

### Running the code locally
- In the terminal command line enter:
   1. `git clone https://github.com/brettcutt/the-chef-desire.git`
   2. `sudo pip3 install flask`
   3. `sudo pip3 install pymongo`
   4. `sudo pip3 install flask_pymongo`
- Set up a database in mlabs
   1. Create an account.
   2. Create a new deployment (database). The name of the database will be the name entered into the `|database name|` in steps below.
   3. Create a new user. Set a username and password for that database.
   4. Take note of the MongoDB URI after creating a user e.g. `mongodb://|yourusername|:|yourpassword|@ds249233.mlab.com:49233/|yourdatabasename|`. This will be entered in steps below.
   4. Create 4 collections called `'recipe', 'allergens', 'cuisines' `and` 'user_details'`.
   5. In `the-meal-ponderer/data` directory copy the data from `allergen_category.json` and `allergen_category.json` and paste it into the `allergens` and `cuisines` collection as a document.
- In the project folder create a `config.py` file.
   1. In the terminal line enter `echo 'config.py' > gitignore` to hide the `config.py` file.
   2. In the config.py file enter the following: 
    ```
     DB_CONFIG = {   
        ' MONGO_DBNAME ':'|database name|',
        ' MONGO_URI ': 'mongodb://|username|:|password|@ds249233.mlab.com:49233/|database name|'
        ' SECRET_KEY ': '|secret key|'
    }
    ```
    3. In app.py, set the app.config variables to the variables set in the config.py file
    ```
    import config
    app.config["MONGO_DBNAME"] = config.DB_CONFIG['MONGO_DBNAME']
    app.config["MONGO_URI"] = config.DB_CONFIG['MONGO_URI']
    app.secret_key = config.DB_CONFIG['SECRET_KEY']
    ```
- In the terminal line enter:
  - `python3 app.py` to run the app.
___
### Credits
#### Bits and pieces of code that helped me along the way.
- jquery function to add input fields   
   - https://www.youtube.com/watch?v=jSSRMC0F6u8
   
- how to order a collection by a specific field.
   - https://docs.mongodb.com/manual/reference/operator/meta/orderby/

- Finding an ingredient by upper or lower case 
   - https://stackoverflow.com/questions/10700921/case-insensitive-search-with-in

- validate that at least one field is filled out in the advanced search
   - https://www.sitepoint.com/community/t/validation-check-to-make-sure-at-least-one-field-is-filled-out/2329

- request.referrer
   - https://stackoverflow.com/questions/45040365/flask-redirect-to-page-then-come-back

- multiple pymongo queries: find with "and" and "or"  
   - https://stackoverflow.com/questions/40388657/query-mongodb-with-and-and-multiple-or

- This helped me to disable scrolling when the search form appears.
   - https://stackoverflow.com/questions/3656592/how-to-programmatically-disable-page-scrolling-with-jquery

- Scroll to top
   - https://stackoverflow.com/questions/5580350/jquery-cross-browser-scroll-to-top-with-animation

- Return documents without specific attribute
   - https://docs.mongodb.com/manual/reference/operator/query/nin/

#### The information of the recipes
- the recipe: name, cuisine, ingredients, instructions and images came from `https://www.themealdb.com/api.php`
- The recipe: prep time, cook time and servings came from external recipe sites.  
- the recipe descriptions were googled by their recipe name and obtained from wikipedia 


#### media
- background picture
   - https://pxhere.com/en/photo/1369811

- Font Awesome
   - GitHub icon
   - plus and remove button icons
   - timer and cutlery icons

### Acknowledgements
- My mentor Mossa Hassan
   - Credit is due to my mentor when it came to the unit testing. There were alot emails trying to get particular tests to pass, The following is that code that is implementd in basic_test.py.
   - content_type='multipart/form-data'
   - data=dict( "list" )
   - register_username='m' + str(random.randint(1,1000))
   - print(dir(response))
   - 
- Slack Forum (Code Institute Student)
   - Thanks to a discussion in the forum it allowed me to follow along to the idea of setting my app config variables
   in a config.py file and importing that into the app.py file.


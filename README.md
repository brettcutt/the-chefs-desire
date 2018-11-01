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
- These pages only have the form inputs for the information of the recipe the user is adding or editing.
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
   -Created a new app
- In the terminal command line enter:
   - `heroku login` Entered username and password.   
   - `git init` to Intilised a git repository.
   - `git remote add heroku https://the-chefs-desire.herokuapp.com/` to link the GitHub repository to the Heroku app.
   - `pip3 freeze --local > requirements.txt` Creates a .txt file which tells Heroku what dependencies the project is using.
   - `echo web: python run.py >procfile` Tells Heroku that this project is a web app and that "app.py" is going the run it.
   - `ps:scale web=1`
   - `git add`
   - `git commit -m "message"`
  -  `git push -u heroku master` pushes the project to Heroku.
- In heroku
   - Go to the project > setting > config vars
   - IP = `0.0.0.0`
   - PORT =  `8080`
   - More > restart all dynos

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
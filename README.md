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
#### Manual testing
- A. Base.html(header and footer)
  1. Checking all navigation buttons redirect to the appropriate pages.
  2. Non signed in users navbar displays 'register' and 'sign in' buttons.
  3. signed in users navbar displays 'my recipes' and 'log out' buttons.
  4. The log out button, successfully logs out the user from their account.
  5. Register and sign in buttons make the appropriate pop up box appear.
  6. The logo redirects to the index page.
  7. The GitHub icon opens a new page to my GitHub repository.

- B. Registration form
  1. The registration form records all user data and sends to the MongoDB database in the 'users_details' collection. 
  2. After filling out the form the user is redirected to a personal 'my recipes' page.
  3. If the requested username is already in the database, the form will not submit and a flash message will display telling the user.
  4. If the two password input fields don't match, the form won't be submitted and a flash message will display letting the user know.
  5. The close button closes the registration form.

- C. Sign In Form
  1. An incorrect username, password or both displays a flash message telling the user.
  2. Successful input of a username and password redirect to the users to the 'my recipes' page.
  3. The close button closes the sign in form.

- D. Search forms/ buttons
  1. Each search button opens the appropriate search form.
  2. The same button becomes highlighted on click and unhighlight on form close or other button click.
  3. When criteria is searched, the page is redirected to the 'search results' page.
  4. The appropriate search criteria was found.
  5. The close button closes the search form.
  6. On mobile there is only a 'Define search' button.
 
- E. Index
  1. The index image when clicked redirects to that images single recipe page.
  2. Non signed in users have 'enter' and 'register' buttons displaying under the tagline.
  3. Signed in users have only the 'enter' button displaying under the tagline.

- F. Recipes
  1. All Images that are clicked on redirect to that recipes 'single recipe' page.
  2. The 'See All' button redirect to more recipes of that sub category.

- G. My Recipes
  1. If no recipes have been created, this page has text telling the user that.
  2. The 'add recipe' button redirects to the add recipes page.
  3. A user with added recipes can see them on this page and a number of how many recipes added is shown.
  4. Clicking on a recipe redirects to that recipes 'single recipe' page.
 
- H. Single Recipe
  1. All the correct information is displayed.
  2. If the user is also the one who added the recipe, 'delete' and 'edit' buttons appear on the page.
  3. Per session if the recipes is visited the view count goes up one point.
  4. A non account holder cannot like a recipe but will receive a message telling them that if they want to like a recipe, they need
to register. Under the message is a 'register' and 'close' button. A click on the register button smooth scrolls to the top
of the page and opens the register form.
  5. An account holder can only like a recipe once and if the recipe is liked, the heart is disabled and remains solid red.
  6. If the user is also the one who added the recipe, The like button is disabled and the view count remains the same.

- I. Add Recipe
  1. All information inputed into the form successfully gets sent to the database.
  2. The user is redirected to their newly created recipe in 'single recipe'.

- J. Edit Recipe
  1. All the recipes existing values are pre loaded into the correct input fields.
  2. The Add and Remove buttons work on their input fields.
  3. On submission all the correct values are stored or deleted from the database.
  4. On submission the page is redirected to that recipes 'single recipe' page.

|Pass|Fail|
|:--:|:--:|
|P|F|

|     |Chrome|FireFox|Edge|Opera|Safari|Mobile|
|:---|:----:|:-----:|:--:|:---:|:----:|:----:|
|**A. i**|      P|P|P|P|P|P|
|**A. ii**|     P|P|P|P|P|P|
|**A. iii**|    P|P|P|P|P|P|
|**A. iv**|     P|P|P|P|P|P|
|**A. v**|      P|P|P|P|P|P|
|**A. vi**|     P|P|P|P|P|P|       
|**A. vii**|    P|P|P|P|P|P|
|**B. i**|      P|P|P|P|P|P|
|**B. ii**|     P|P|P|P|P|P|
|**B. iii**|    P|P|P|P|P|P|
|**B. iv**|     P|P|P|P|P|P|
|**B. v**|      P|P|P|P|P|P|
|**C. i**|      P|P|P|P|P|P|
|**C. ii**|     P|P|P|P|P|P|
|**C. iii**|    P|P|P|P|P|P|
|**D. i**|      P|P|P|P|P|P|
|**D. ii**|     P|P|P|P|P|P|
|**D. iii**|    P|P|P|P|P|P|
|**D. iv**|     P|P|P|P|P|P|
|**D. v**|      P|P|P|P|P|P|
|**D. vi**|     P|P|P|P|P|P|
|**E. i**|      P|P|P|P|P|P|
|**E. ii**|     P|P|P|P|P|P|
|**E. iii**|    P|P|P|P|P|P|
|**F. i**|      P|P|P|P|P|P|
|**F. ii**|     P|P|P|P|P|P|
|**G. i**|      P|P|P|P|P|P|
|**G. ii**|     P|P|P|P|P|P|
|**G. iii**|    P|P|P|P|P|P|
|**G. iv**|     P|P|P|P|P|P|
|**H. i**|      P|P|P|P|P|P|
|**H. ii**|     P|P|P|P|P|P|
|**H. iii**|    P|P|P|P|P|P|
|**H. iv**|     P|P|P|P|**F**|P|
|**H. v**|      P|P|P|P|**F**|P|
|**H. vi**|     P|P|P|P|**F**|P|
|**I. i**|      P|P|P|P|P|P|
|**I. ii**|     P|P|P|P|P|P|
|**I. i**|      P|P|P|P|P|P|
|**I. ii**|     P|P|P|P|**F**|P|
|**I. iii**|    P|P|P|P|P|P|
|**I. iv**|     P|P|P|P|P|P|

##### Notes:
- Safari:
  - I'm running safari on windows, which the last update was back in 2012. This would suggest that this version of browser doesn't support some css or jquery attributes the same as other browsers.   
  - The jquery add and remove buttons in the add and edit pages didn't work. I couldn't add more input fields to the cuisine, ingredient and instruction categories. 
  - The font-size was bigger than usual, which made the containers larger and out of place.
  - This font awesome hearts also were not supported amd didn't show.

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
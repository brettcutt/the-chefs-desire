# Manual Testing
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

## Index page(login)
![registration form](https://github.com/brettcutt/the-chefs-desire/blob/master/static/images/test-registration.jpeg?raw=true "registration form")
/* Checks if at least one form field is filled out in the advanced search model*/
function anyvalidate() {
    
/*verifies if any of the check boxes are checked */    
var test = form.find_allergen;
var test2 = false
var i;
for (i = 0; i < test.length; i++) {
  if (test[i].checked == true) {
    test2 = true;
  }
}    
/*Verifies if any of the form fields are empty to send an alert*/
if (       form.find_ingredient.value == ""
	&& test2 == false
	&& form.find_cuisine.value == "") {
document.getElementById('no-search-item').innerHTML = "At least one field should be filled out. .";
     return false;
	 }
	 }
	 

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
    if (form.find_ingredient.value == "" &&
        test2 == false &&
        form.find_cuisine.value == "") {
        document.getElementById('no-search-item').innerHTML = "At least one field should be filled out. .";
        return false;
    }
}

/*The code below for checkImageExist is from 
	 https://stackoverflow.com/questions/24577534/javascript-how-to-check-if-a-typed-image-url-really-exists
    written by eithed. 
    This is used to validate the image address in the add and edit html pages.
    Prevents form submission if the address is false*/

function checkImageExists() {
    add_form.image.className = "valid"
    document.getElementById('image-validation').innerHTML = "";
    var file_path = add_form.image.value;
    var img = document.createElement('img');
    img.setAttribute('src', file_path);
    img.onerror = function() {

        document.getElementById('image-validation').innerHTML = "The image address is incorrect.";
        add_form.image.className = "notvalid"
        return false
    }
}

function valid_image() {

    if (add_form.image.className == "notvalid") {
        document.getElementById('image-validation').innerHTML = "The image address is incorrect.";
        return false
    }
    else {

    }
}

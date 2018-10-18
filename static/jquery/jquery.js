$(document).ready( function() {
    
    $("#ingredient_btn").click(function() {
        $("#ingredient_search").show()
        $("#cuisine_search").hide()
        $("#allergen_search").hide()
        $("#allergen_and_cuisine_search").hide()
        $(this).addClass("choice")
        $("#cuisine_btn").removeClass("choice")
        $("#allergen_btn").removeClass("choice")
        $("#allergen_and_cuisine_btn").removeClass("choice")
    })
    
    $("#cuisine_btn").click(function() {
        $("#ingredient_search").hide()
        $("#cuisine_search").show()
        $("#allergen_search").hide()
        $("#allergen_and_cuisine_search").hide()
        $("#ingredient_btn").removeClass("choice")
        $(this).addClass("choice")
        $("#allergen_btn").removeClass("choice")
        $("#allergen_and_cuisine_btn").removeClass("choice")
    })
    
    $("#allergen_btn").click(function() {
        $("#ingredient_search").hide()
        $("#cuisine_search").hide()
        $("#allergen_search").show()
        $("#allergen_and_cuisine_search").hide()
        $("#ingredient_btn").removeClass("choice")
        $("#cuisine_btn").removeClass("choice")
        $(this).addClass("choice")
        $("#allergen_and_cuisine_btn").removeClass("choice")
    })
    
    $("#allergen_and_cuisine_btn").click(function() {
        $("#ingredient_search").hide()
        $("#allergen_search").hide()
        $("#cuisine_search").hide()
        $("#allergen_and_cuisine_search").show()
        $("#ingredient_btn").removeClass("choice")
        $("#cuisine_btn").removeClass("choice")
        $("#allergen_btn").removeClass("choice")
        $(this).addClass("choice")
    })
    $(".close-btn").on('click', function() {
        $("#allergen_search").hide()
        $("#cuisine_search").hide()
        $("#allergen_and_cuisine_search").hide()
        $("#ingredient_search").hide()
        $("#ingredient_btn").removeClass("choice")
        $("#cuisine_btn").removeClass("choice")
        $("#allergen_btn").removeClass("choice")
        $("#allergen_and_cuisine_btn").removeClass("choice")
        
    })
    
    
/*Add input field for instruction and ingredients, also adds the add and remove buttons*/    
   
    $("body").on('click','.duplicate', function(){
        
        var id_name = $(this).parent().children('input').attr("name");
        
        if ($(this).attr('id') == 'first') {
            $(this).append().after(
            '<br><input type="text" name="' + id_name +'" class="' + id_name +'" placeholder="Add"/> <i class="fas fa-plus-circle duplicate pointer">Add</i>' +
            ' <i class="fas fa-plus-circle remove_duplicate pointer">Remove</i>');
        } 
        
        else 
        {
            $(this).next().append().after(
            '<br><input type="text" name="' + id_name +'" class="' + id_name +'" placeholder="Add"/> <i class="fas fa-plus-circle duplicate pointer">Add</i>' +
            ' <i class="fas fa-plus-circle remove_duplicate pointer">Remove</i>');
        }
        
    });
    
    $("body").on('click','.remove_duplicate', function(){
        $(this).prev().remove();
        $(this).prev().remove();
        $(this).prev().remove();
        $(this).remove();
    });
    
    
/*Select cuisine and allergens, also addds the remove*/
    
    $("body").on('click','.duplicate_select', function(){
        
    var select_remove_button = ' <i class="fas fa-plus-circle remove_select pointer">Remove</i><br>';
    
        if ($(this).attr('id') == 'add_cuisine') {
            $("#cuisine").clone().appendTo(".cuisine_container").after(select_remove_button)
        }
        else if ($(this).attr('id') == 'add_allergen') {
            $("#allergens").clone().appendTo(".allergens_container").after(select_remove_button)
        }
    });
    
    $("body").on('click','.remove_select', function(){
        $(this).prev().remove();
        $(this).prev().remove();
        $(this).remove();
    });
    
    
});
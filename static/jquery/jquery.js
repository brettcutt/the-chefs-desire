$(document).ready( function() {
    
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
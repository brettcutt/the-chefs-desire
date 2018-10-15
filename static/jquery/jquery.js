$(document).ready( function() {
    
    
    
    $("body").on('click','.duplicate', function(){
        var id_name = $(this).parent().children('input').attr("name");
        
        $(this).parent().children().last().append().after(
            '<br><input type="text" name="' + id_name +'" class="allergens" placeholder="Add"/> <i class="fas fa-plus-circle duplicate pointer">Add</i>' +
            ' <i class="fas fa-plus-circle remove_duplicate pointer">Remove</i>');
    });
    
    $("body").on('click','.remove_duplicate', function(){
        $(this).prev().remove();
        $(this).prev().remove();
        $(this).prev().remove();
        $(this).remove();
    });
    
});
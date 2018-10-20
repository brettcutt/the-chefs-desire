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
            '<br><input type="text" name="' + id_name +'" class="' + id_name +'" placeholder="Add"/>'+
            ' <i class="material-icons duplicate pointer">add</i>' +
            ' <i class="material-icons remove_duplicate pointer">remove</i>');
        } 
        
        else 
        {
            $(this).prev().prev().prev().append().after(
            '<br><input type="text" name="' + id_name +'" class="' + id_name +'" placeholder="Add"/>'+
            ' <i class="material-icons duplicate pointer">add</i>' +
            ' <i class="material-icons remove_duplicate pointer">remove</i>');
        }
        
    });
    
    $("body").on('click','.remove_duplicate', function(){
        $(this).prev().remove();
        $(this).prev().remove();
        $(this).prev().remove();
        $(this).remove();
    });
    
    
/*Select cuisine on add and edit html*/
    
    $("body").on('click','.duplicate_select', function(){
        
    var select_remove_button = ' <i class="material-icons remove_select pointer">remove</i><br>';
    
        if ($(this).attr('id') == 'add_cuisine') {
            $("#cuisine").clone().appendTo(".cuisine_container").before(select_remove_button)
            $(this).appendTo(".cuisine_container")
            $('.duplicate_select').addClass("add-fourpx")
        }
    });
    
    $("body").on('click','.remove_select', function(){
        $(this).prev().remove();
        $(this).next().remove();
        $(this).remove();
    });
    
/*Select allergen on add and edit html*/

    $(".nuts:not(:first)").parent().remove();
    $(".dairy:not(:first)").parent().remove();
    $(".penuts:not(:first)").parent().remove();
    $(".eggs:not(:first)").parent().remove();
    $(".crustacean:not(:first)").parent().remove();
    $(".wheat:not(:first)").parent().remove();
    $(".soybeans:not(:first)").parent().remove();
    
    
    if ($('.duplicate_select').prev().prev().hasClass('remove_select')) {
                $('.duplicate_select').prev().remove()
                $('.duplicate_select').prev().remove()
                
            }
    
});
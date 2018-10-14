$(document).ready( function() {
    var count = 1
    $('#duplicate').click(function(){
        $('#duplicate').append().before(
            '<br><input type="text" name="special_diet" id = "special_diet_' + count + '" class="special_diet" placeholder="special diet"/>');
            count +=1;
    });
    
    $('#duplicate2').click(function(){
        $('#duplicate2').append().before(
            '<br><input type="text" name="ingredients" id = "ingredients'+ count +'" class="ingredients" placeholder="ingredient"/>');
        count += 1;
    });
    
    $('#duplicate3').click(function(){
        $('#duplicate3').append().before(
            '<br><input type="text" name="instructions" id = "instructions'+ count +'" class="instructions" placeholder="Recipe Instructions"/>');
        count += 1;
    });
});
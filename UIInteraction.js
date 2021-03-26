$(document).ready(

    $(".manga_dropdown").change(function(){
        var value = $(".manga_dropdown").val();

        $.ajax({
            type: "POST"
            contentType: "application/json;charset=utf-8"
            url: "/choose_manga/"
            traditional: "true"
            data: JSON.stringify({value})
            dataType: "json"
        })
    });


);

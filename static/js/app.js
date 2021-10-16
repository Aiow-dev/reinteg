$(".integral__form button").on("click", function() {
    $(".integral__form .error").text();
    setTimeout(function() {
        if($(".integral__form input:focus").length > 0) {
            $(".integral__form .error").text("Заполните поле: " + $(".integral__form input:focus").data("name"));
        }
    }, 100)
})

$(".integral__form").submit(function(e){
    // e.preventDefault();
    console.log($(this).serialize());
    $.ajax({
        type: "POST",
        url: $(this).attr("action"),
        data: $(this).serialize(),
        success: function(data){
            console.log(data);
        },
        error: function(jqXHR){
            console.log(jqXHR.statusText);
        }
    })
    var received_data = data;
    console.log(received_data);
})

$(document).ready(function() {
    $("#method").val(localStorage.getItem("method"));
    console.log(localStorage.getItem("method"));
    if(localStorage.getItem("method") == "trapezoid_method_accuracy") {
        $(".segments").after(`<input type="number" data-name="Точность" 
        step="any" class="accuracy" name="accuracy" placeholder="Точность" required="">`)
    } else {
        $(".accuracy").remove();
    }
})
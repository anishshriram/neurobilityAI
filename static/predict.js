let base64Image;
$("#image-selector").change(function() {
    let reader = new FileReader();
    reader.onload = function(e){
        let dataURL = reader.result;
        $("#selected-image").attr("src", dataURL);
        base64Image = dataURL.replace("data:image/png;base64,", "");
        console.log(base64Image)
    }
    reader.readAsDataURL($("#image-selector")[0].files[0]);
    $("#predicted-digit").text("");
});

$("#predict-button").click(function(event){
    let message = {
        image: base64Image
    }
    console.log(message);
    $.post("http://localhost:5000/predict", JSON.stringify(message), function(response){
        $("#predicted-digit").text(response.prediction);
        console.log(response);
    });
});
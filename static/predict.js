// The base64 image variable
let base64Image;
// Calling the jquery change function
$("#image-selector").change(function() {
    // Reader object to read the contents of the file the user select
    let reader = new FileReader();
    reader.onload = function(e){
        // URL that represents the image as a base64 encoded string
        let dataURL = reader.result;
        // Displays the image on the page (gives the html source a URL for the image)
        $("#selected-image").attr("src", dataURL);
        // Strips the url portion of the image for just the base64 portion
        base64Image = dataURL.replace("data:image/png;base64,", "");
    }
    // Loads and reads the image, triggering the onload handler
    reader.readAsDataURL($("#image-selector")[0].files[0]);
    // Clearing any previous text
    $("#predicted-digit").text("");
});

// When the predict button is clicked
$("#predict-button").click(function(event){
    // Message object is the base64 image
    let message = {
        image: base64Image
    }

    // Make post request with the message converted to json, specify what to do
    $.post("http://localhost:5000/predict", JSON.stringify(message), function(response){
        // Response will give the likely number (the key is prediction)
        $("#predicted-digit").text(response.prediction);
    });
});
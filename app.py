import base64
import numpy as np
import io
from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask

# Creating an instance of the Flask class
app = Flask(__name__)


# Function to actually get the model
def get_model():
    global model
    # Loads the mnist model
    model = load_model('model.h5')
    # print("model loaded")


# Accepts a image and preprocesses it so that it is accepted
def preprocess_image(image):
    # Makes sure the image is in black and white
    if image.mode != "L":
        image = image.convert("L")
    # Resizes image
    image = image.resize((28, 28))
    # Converts the image into an array
    image = img_to_array(image)
    # Expands the dimensions of the image
    image = np.expand_dims(image, axis=0)
    return image


# print(" loading keras model...")
# Loads the model
get_model()


# The app decorator tells flask what endpoint the user should be at to access functionality
# Methods parameter tells us what kind of HTTP request is allows - POST to send data
@app.route("/predict", methods=["POST"])
# Function to define what to do when a post request is sent
def predict():
    # .get_json gives us the message (the image) from the web app
    message = request.get_json(force=True)
    # Receiving json data - base64 encoded
    encoded = message['image']
    # Decoding the image
    decoded = base64.b64decode(encoded)
    # PIL image, wrapping the decoded image with BytesIO
    image = Image.open(io.BytesIO(decoded))
    # Process the image
    processed_image = preprocess_image(image)

    # Model will predict, is an array that has the probability that the image is each digit
    pred_temp = model.predict(processed_image)
    # Chooses the greatest value from the array - which is the most likely digit in the image
    prediction = int(np.argmax(pred_temp))

    # Response variable, the response to send back to the web app
    response = {
        # The predicted value
        'prediction': prediction
    }

    # Returns the response jsonified
    return jsonify(response)

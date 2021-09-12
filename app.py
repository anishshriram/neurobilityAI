import base64
import numpy as np
import io
from PIL import Image
import keras
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask
import pickle

from matplotlib.pyplot import axis

app = Flask(__name__)


def get_model():
    global model
    model = load_model('model.h5')
    print("model loaded")


def preprocess_image(image):
    if image.mode != "L":
        image = image.convert("L")
    image = image.resize((28, 28))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image


print(" loading keras model...")
get_model()


@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image)

    pred_temp = model.predict(processed_image)
    prediction = int(np.argmax(pred_temp))

    response = {
        'prediction': prediction
    }

    return jsonify(response)

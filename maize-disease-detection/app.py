# Import necessary libraries
from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import os
import io
import requests
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from keras.models import load_model

# load model
model = load_model("model/maize.h5")
binary_model = load_model("model/binary.h5")

print('@@ Model loaded')


def check_img(cott_plant):
    img = Image.open(cott_plant)


    img_array = np.array(img)
    # Resize the image to 256x256
    img_array = tf.image.resize(img_array, [256, 256])

    # Normalize pixel values
    img_array = img_array / 256

    # Expand dimensions to match the input shape of the model (batch size of 1)
    img_array = np.expand_dims(img_array, axis=0)

    # Make a prediction
    prediction = binary_model.predict(img_array)

    # Get the predicted class
    # predicted_class = np.argmax(prediction)
    print(prediction)
    return prediction[0][0] < 0.01

def pred_cot_dieas(cott_plant):

    if check_img(cott_plant):
        test_image = load_img(cott_plant, target_size=(150, 150))  # load image
        print("@@ Got Image for prediction")

        test_image = img_to_array(test_image) / 255  # convert image to np array and normalize
        test_image = np.expand_dims(test_image, axis=0)  # change dimention 3D to 4D

        result = model.predict(test_image).round(3)  # predict diseased palnt or not
        print('@@ Raw result = ', result)

        pred = np.argmax(result)  # get the index of max value


        if pred == 0:
            return "Cercospora leaf spot Gray leaf spot", 'Cercospora_leaf_spot Gray_leaf_spot.html'  # if index 0 burned leaf
        elif pred == 1:
            return 'Common rust ', 'Common_rust_.html'  # # if index 1
        elif pred == 2:
            return 'Northern Leaf Blight', 'Northern_Leaf_Blight.html'  # if index 2  fresh leaf
        elif pred == 3:
            return 'healthy', 'healthy.html'
        else:
            return "Healthy ", 'healthy.html'  # if index 3
    else:
        return "Can't Identify Maize leaf in image", 'error.html'



# ------------>>pred_cot_dieas<<--end


# Create flask instance
app = Flask(__name__)


# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']  # fet input
        filename = file.filename
        print("@@ Input posted = ", filename)

        file_path = os.path.join('static/useruploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_cot_dieas(cott_plant=file_path)
        # if pred == "Can't Identify Maize leaf in image":
        #     return output_page
        return render_template(output_page, pred_output=pred, user_image=file_path)


# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False, port=5001, debug=True)

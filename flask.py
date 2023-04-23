# import necessary libraries
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np

# import custom modules
from preprocess_data import preprocess_data
from train_model import train_model

# load the trained model
with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

# create a new Flask app instance
app = Flask(__name__)

# define a basic route
@app.route('/', methods=['GET'])
def home():
    return "Welcome to my soccer betting bot API!"

# define an endpoint for receiving prediction requests
@app.route('/predict', methods=['POST'])
def predict():
    # extract data from request
    json_data = request.get_json()
    input_data = pd.DataFrame(json_data, index=[0])

    # preprocess the input data
    preprocessed_data = preprocess_data(input_data)

    # make predictions using the preprocessed data
    predictions = model.predict(preprocessed_data)

    # create a dictionary response containing the predictions
    response = {'predictions': predictions.tolist()}

    # return the response as JSON
    return jsonify(response)

# start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

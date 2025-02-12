import pickle
import numpy as np
from flask import Flask, request, jsonify   # request: for http request, jsonify: convert request to json

# Load the trained model
with open('iris_model.pkl', "rb") as file:
    model = pickle.load(file)


# Initialize Flask app
app = Flask(__name__)

# Define home route
@app.route('/')
def home():
    return 'Welcome the the Iris Prediction API! Use the /predict endpoint to make predictions'


@app.route("/predict", methods=["POST"])
def predict():
    # Get the data from the request
    data = request.get_json(force=True)
    
    # Convert features to numpy array
    features = np.array(data['features']).reshape(1,-1)
    
    # Make prediction
    prediction = model.predict(features)
    
    # Map numberic prediction to class name
    species = {0:'Iris-setosa', 1:'Iris-versicolor', 2:'Iris-virginica'}
    predicted_species = species[int(prediction[0])]

    # Send back the prediction as JSON
    return jsonify({"prediction": int(prediction[0]), 'species': predicted_species})


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

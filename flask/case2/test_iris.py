
# 1. test if the model is predicting correctly to understand how it is expecting input to be passed
# 2. Run iris_flask_execute file to get the API up and running
# 3. In a different terminal, run the iris_flask_serve file

import pickle
import numpy as np


# Load the trained model
with open('iris_model.pkl', 'rb') as file:
    model = pickle.load(file)


features = np.array([5.1,1.0,1.5,3]) # giving 4 inputs as iris takes 4 args


# Make prediction
prediction = model.predict([features])
print(prediction)







from datetime import date
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle 

# Model Serialization: coverting trained models to serialized files that have IP (intellectual property)
# pickle - converts a python object into a byte stream. can pickle models, data etc to save and reload them later
# onnx file Open Neural Network Exchange -> deep learning
# HDF5 - tensorflow
# PMML - Predictive Model Markup Language

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model to a file
with open('iris_model.pkl', 'wb') as file:
    pickle.dump(model, file)
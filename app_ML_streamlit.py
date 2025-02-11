# Pull datasets from OpenML: https://openml.org/ and create ML model
# train a ML model -> then deploy it for users to use it

import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_openml  # downloads data from openml website
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


# load dataset
housing = fetch_openml(name='house_prices', as_frame=True)
X = housing.data[['GrLivArea', 'YearBuilt']]
y = housing.target


# train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)


# Streamlit app
st.title('Housing Price Prediction')

GrLivArea = st.number_input('Above grade living area in square feet', value = 1500)
YearBuilt = st.number_input('Original construction date', value = 2000)

input_data = pd.DataFrame({'GrLivArea': [GrLivArea], 'YearBuilt':[YearBuilt]})

if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Predicted House Price: ${prediction[0]:.2f}')






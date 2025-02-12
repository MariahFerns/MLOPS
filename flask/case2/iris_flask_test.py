# Code to test the Flask app deployment
# can use POSTMAN OR CURL to test as well
# CURL   :curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
# POSTMAN: POST = http://127.0.0.1:5000/predict, body:{"features": [5.1, 3.5, 1.4, 0.2]} 

import requests
import json

# URL of the Flask API
url = 'http://127.0.0.1:5000/predict'

# Sample input data
data = {
    'features': [5,2,2,1]
}

# Send POST request
response = requests.post(url, json=data)


# Print response
if response.status_code == 200:
    print('Prediction', response.json())
else:
    print(f'Error: {response.status_code}, {response.text}')

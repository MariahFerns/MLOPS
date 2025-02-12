from flask import Flask

# create instance of Flask
app = Flask(__name__) # __name__ : root dir

@app.route('/')   # decorator -> function hello is connected the root url
def hello():
    return 'Hello, Welcome to the MLOPS session!'

if __name__ == '__main__':  # check if script is running directly
    app.run(debug=True)     # run app in debug mode
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, your sample flask app is working fine!!! Congoz!!'

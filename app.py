from flask import Flask
app=Flask(__name__)

@app.route('/') #route point. Base point to our application
def hello_world():
    return 'Welcome, to our first DevOps Flask Application'

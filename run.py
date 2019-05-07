# First thing we want to do is import os so that we'll have access to the environment variables
import os
from flask import Flask

# Here we initialise our application
app = Flask(__name__)

@app.route('/')
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"
    
@app.route('/<username>')
def user(username):
    return "Hi" + username
    
@app.route('/<username>/<message>')
def send_message(username, message):
    return "{0}: {1}".format(username, message)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
# First thing we want to do is import os so that we'll have access to the environment variables
import os
from flask import Flask

# Here we initialise our application
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello there!</h1>"
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
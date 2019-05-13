# First thing we want to do is import os so that we'll have access to the environment variables
import os
#  the datetime library, which is a built in module in Python's standard library that allows us to work specifically with dates and times
# he request module, which will handle our username form, and the session module, which will handle the session variables
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for


# Here we initialise our application
app = Flask(__name__)
# "randomstring123" is left there as the second argument because this becomes the default value if Flask can't find a variable called SECRET
app.secret_key = os.getenv("SECRET", "randomstring123")
messages = []


def add_message(username, message):
    """Add messages to the `messages` list"""
    
    # The strftime() method takes a date/time object and then converts that to a string according to a given format
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})


@app.route('/', methods = ["Get", "POST"])
def index():
    """Main page with instructions"""
    
    if request.method == "POST":
        session["username"] = request.form["username"]
        
    # if the username variable is set, then instead of returning our index.html template, 
    # we're going to redirect to the contents of the session username variable
    if "username" in session:
        # This is so that if we change the URL, then we don't have to worry about what redirects may be calling it directly
        return redirect(url_for("user", username=session["username"] ))
    
    return render_template("index.html")
    

@app.route('/chat/<username>', methods = ["GET", "POST"])
def user(username):
    """Add and display chat messages"""
    
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        # The redirect function here makes sure the messages are not continually being added to the list.
        return redirect(url_for("user", username=session["username"] ))
    
    return render_template("chat.html", username = username, chat_messages = messages)
    
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', '5000')), debug=False)
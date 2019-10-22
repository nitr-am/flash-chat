import os #This will give us acces to the enviornment variables
from flask import Flask

app = Flask(__name__) #This is a new application.


@app.route("/") #This is the app route decorator
def index():  #This is the funcion that is going to be bound to our decorator.
    """Main page with instructions"""
    return "To send a message use: /USERNAME/MESSAGE"

@app.route("/<username>")
def user(username):
    return "Hi " + username

@app.route("/<username>/<message>")
def send_message(username, message):
    return "{0}: {1}".format(username, message)

if __name__ =="__main__":
    app.run(host=os.getenv("IP"),
       port=os.getenv("PORT"),
       debug=True)
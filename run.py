import os #This will give us acces to the enviornment variables
from flask import Flask

app = Flask(__name__) #This is a new application.


@app.route("/") #This is the app route decorator
def index():  #This is the funcion that is going to be bound to our decorator.
    return "<h1>Hello There</h1>"


if __name__ =="__main__":
    app.run(host=os.getenv("IP"),
       port=os.getenv("PORT"),
       debug=True)
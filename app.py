#!/usr/bin/python
from flask import Flask, render_template, request,flash

app = Flask(__name__) #initialise app ( create a class)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


if __name__ == "__main__":
    app.run(debug=True)
        


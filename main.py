#!/bin/python

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about/")
def about():
    return "<h1>ABOUT</h1><p>This is the about page</p>"

@app.route("/admin/")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
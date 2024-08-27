#!/usr/bin/env python3

"""0. Basic Flask app
Start a basic Flask web application
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Display a welcome message"""
    return render_template("0-index.html", title="Welcome to Holberton")

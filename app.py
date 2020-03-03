# General Imports
import imp
import os

# Specific Imports
from flask import Flask, render_template

app = Flask(__name__)

# Main Page
@app.route('/')
def home_page():
    return render_template('index.html')

# Run Website w/o Debug Enabled
def run():
    app.config['TEMPLATES_AUTO_RELOAD'] = False
    app.config['DEBUG'] = False
    app.config['ENV'] = "production"
    app.run()

# Run Website w/ Debug Enabled
def debug():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True
    app.config['ENV'] = "development"
    app.run()
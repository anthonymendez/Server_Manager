# General Imports
import importlib
import os

# Specific Imports
from flask import Flask, render_template, session

# Plugin Header
plugin_folder = "plugins"
main_module = "__init__"
plugin_module = "plugin"
config_file = "config"

# Retrieves all given plugins
def import_plugins():
    plugins = []
    possible_plugins = os.listdir(plugin_folder)
    for i in possible_plugins:
        location = os.path.join(plugin_folder, i)
        if not os.path.isdir(location) or not main_module + ".py" in os.listdir(location):
            continue
        pkg_location = os.path.relpath(location).replace("\\",".")
        info = importlib.import_module('.' + main_module, package=pkg_location)
        print("Adding Plugin " + i)
        plugins.append({"name": i, "info": info})
    return plugins

def consolidate_config():
    new_config = open(config_file+".ini", "w")
    new_config.truncate(0)
    new_config.close()
    new_config = open(config_file + ".ini", "a")
    possible_configs = os.listdir(plugin_folder)
    for i in possible_configs:
        location = os.path.join(plugin_folder, i)
        if not os.path.isdir(location) or not config_file + ".ini" in os.listdir(location):
            continue
        curr_config = open(location + "\\" +config_file + ".ini", "r")
        new_config.write(curr_config.read())
        new_config.write("\n\n")
    new_config.close()

def get_plugins_functions():
    # TODO: Create list of list of functions from each plugin
    plugins = import_plugins()
    for plugin in plugins:
        info = plugin["info"]
        print(info.name())

# Setup
consolidate_config()

# Flask App Setup
app = Flask(__name__)

# Generate Secret Key
app.secret_key = b'BLEHBLEHBLEH'

# Main Page
@app.route('/')
def home_page():
    return render_template('index.html')

# Plugin Injection
@app.context_processor
def inject_plugins():
    get_plugins_functions()
    return dict(loaded_plugins=import_plugins())

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
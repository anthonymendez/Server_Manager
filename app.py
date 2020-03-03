# General Imports
import configparser
import importlib
import os

# Specific Imports
from flask import Flask, render_template, session
from plugins import Jinja_Adapter, Plugin_Adapter

# Plugin Header
plugin_folder = "plugins"
main_module = "__init__"
plugin_config_file = "config"
app_config_file = "app"

# Config Options
config = configparser.ConfigParser()
config_file = "app.ini"
config.read(config_file)
host_ip = config["APP"]["ip"]
host_port = config["APP"]["port"]

# Retrieves all given plugins
def import_plugins():
    plugins = []
    possible_plugins = os.listdir(plugin_folder)
    print("Loading Plugins:")
    for i in possible_plugins:
        location = os.path.join(plugin_folder, i)
        if not os.path.isdir(location) or not main_module + ".py" in os.listdir(location):
            continue
        pkg_location = os.path.relpath(location).replace("\\",".")
        info = importlib.import_module('.' + main_module, package=pkg_location)
        print("\tName:\t\t" + i)
        print("\tLocation:\t" + str(pkg_location))
        info.Plugin = info.start_plugin(i, location)
        info.Jinja = info.start_jinja(info.Plugin)
        plugins.append({"name": i, "info": info})
    print("Plugins Loaded")
    plugin_functions_list = []
    for plugin in plugins:
        info = plugin["info"]
        plugin_functions_list.append(info.Jinja)
    return plugin_functions_list

def consolidate_config():
    new_config = open(plugin_config_file+".ini", "w")
    new_config.truncate(0)
    new_config.close()
    new_config = open(plugin_config_file + ".ini", "a")
    possible_configs = os.listdir(plugin_folder)
    for i in possible_configs:
        location = os.path.join(plugin_folder, i)
        if not os.path.isdir(location) or not plugin_config_file + ".ini" in os.listdir(location):
            continue
        curr_config = open(location + "\\" +plugin_config_file + ".ini", "r")
        new_config.write(curr_config.read())
        new_config.write("\n\n")
    new_config.close()

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
    return dict(loaded_plugins=import_plugins())

# Run Website w/o Debug Enabled
def run():
    app.config['TEMPLATES_AUTO_RELOAD'] = False
    app.config['DEBUG'] = False
    app.config['ENV'] = "production"
    app.run(host=host_ip, port=host_port)

# Run Website w/ Debug Enabled
def debug():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True
    app.config['ENV'] = "development"
    app.run(host=host_ip, port=host_port)
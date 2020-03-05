# General Imports
import configparser
import importlib
import os

# Specific Imports
from flask import Flask, render_template, session, request
from plugins import Jinja_Adapter, Plugin_Adapter
from logging.config import dictConfig

# Configuring Logging

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

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

# Plugins
plugin_list = []
plugin_functions_list = []

# Retrieves all given plugins
def import_plugins():
    possible_plugins = os.listdir(plugin_folder)
    app.logger.info("Loading Plugins:")
    for i in possible_plugins:
        location = os.path.join(plugin_folder, i)
        if not os.path.isdir(location) or not main_module + ".py" in os.listdir(location):
            continue
        pkg_location = os.path.relpath(location).replace("\\",".")
        info = importlib.import_module('.' + main_module, package=pkg_location)
        app.logger.info("\tName:\t\t" + i)
        app.logger.info("\tLocation:\t" + str(pkg_location))
        info.Plugin = info.start_plugin(i, location)
        info.Jinja = info.start_jinja(info.Plugin)
        plugin_list.append({"name": i, "info": info})
    app.logger.info("Plugins Loaded")
    for plugin in plugin_list:
        info = plugin["info"]
        plugin_functions_list.append(info.Jinja)

# Move all configuration files to a single file
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

# Plugin Pages
@app.route("/<path:plugin>/")
def plugin_route(plugin):
    # Get first path to ensure it's a loaded plugin first
    plugin_solo = plugin.split("/")[0]
    if any(p['name'] == plugin_solo for p in plugin_list):
        app.logger.info("Perform HTTP %s for %s.", request.method, plugin_solo)
        app.logger.info("Complete path: %s.", request.path)
        return home_page()
    else:
        app.logger.error("Not a plugin!")
        app.logger.error("Perform HTTP %s for %s.", request.method, plugin_solo)
        app.logger.error("Complete path: %s.", request.path)
        return home_page()

# Plugin Injection
@app.context_processor
def inject_plugins():
    return dict(loaded_plugins=plugin_functions_list)

# Run Website w/o Debug Enabled
def run():
    app.config['TEMPLATES_AUTO_RELOAD'] = False
    app.config['DEBUG'] = False
    app.config['ENV'] = "production"
    import_plugins()
    context = ('cert_4096.pem', 'key_4096.key')
    app.run(host=host_ip, port=host_port, ssl_context=context)

# Run Website w/ Debug Enabled
def debug():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True
    app.config['ENV'] = "development"
    import_plugins()
    app.run(host=host_ip, port=host_port)
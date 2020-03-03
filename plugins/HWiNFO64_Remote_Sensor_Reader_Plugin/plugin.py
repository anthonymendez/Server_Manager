import os
import configparser

default = "HWiNFO64_PLUGIN"
config_filename = "config.ini"
config = configparser.ConfigParser()

def start():
  config.read(config_filename)
  print(config.sections())
  return config

def name():
  config = start()
  return config[default]['name']

def html_id():
  start()
  return config[default]['html id']

def name_link():
  start()
  return config[default]['name link']

def author():
  start()
  return config[default]['author']

def github_link():
  start()
  return config[default]['github link']

def version():
  start()
  return config[default]['version']

def render_template():
    return "Test"
import configparser

default = "PLUGIN_DEBUG_EXAMPLE"
config = configparser.ConfigParser()

def start():
  config.read("config.ini")

def name():
  start()
  print("Getting name!")
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
    return """
        <p>
          Plugin Debug Example Main contents!
        </p>
        <p>
          Shows you how your plugin could look!
        </p>"""

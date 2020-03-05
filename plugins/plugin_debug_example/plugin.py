import os
from flask import render_template
from plugins.plugin_adapter import Plugin_Adapter
from random import random

class Plugin(Plugin_Adapter):
  
  def __init__(self, name, location):
    self.default = "PLUGIN_DEBUG_EXAMPLE"
    self.default_template = "plugin_debug_example.html"
    super().__init__(name, location)

  def plugin_route(self, app, request):
    app.logger.info("Received HTTP %s for %s.", request.method, self.get_plugin_name())
    subpath_list = request.path.split("/")
    app.logger.info(subpath_list)
    if (len(subpath_list) == 4 and subpath_list[1] == self.get_plugin_name() and subpath_list[2] == "get_test"):
      return str(random())
    return self.get_plugin_name() + " " + request.method

  def name(self):
    return super().read_config(self.default, 'name')

  def html_id(self):
    return super().read_config(self.default, 'html id')

  def name_link(self):
    return super().read_config(self.default, 'name link')

  def author(self):
    return super().read_config(self.default, 'author')

  def github_link(self):
    return super().read_config(self.default, 'github link')

  def version(self):
    return super().read_config(self.default, 'version')

  def render_template(self):
    return self.default_template

  def folder_name(self):
    return self.get_location()

def start_plugin(name, location):
  return Plugin(name, location)
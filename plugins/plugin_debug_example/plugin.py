import os
from flask import render_template
from plugins.plugin_adapter import Plugin_Adapter

class Plugin(Plugin_Adapter):
  
  def __init__(self, name, location):
    self.default = "PLUGIN_DEBUG_EXAMPLE"
    self.default_template = "plugin_template.html"
    super().__init__(name, location)

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

def start(name, location):
  return Plugin(name, location)
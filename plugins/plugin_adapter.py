import flask
import configparser
import os

from abc import ABC, abstractmethod

class Plugin_Adapter(ABC):
  

  @abstractmethod
  def __init__(self, plugin_name, location):
    self.set_plugin_name(plugin_name)
    self.set_location(location)

  @classmethod
  def set_plugin_name(cls, plugin_name_):
    cls.plugin_name = plugin_name_

  @classmethod
  def get_plugin_name(cls):
    return cls.plugin_name

  @classmethod
  def set_location(cls, location_):
    cls.location = location_

  @classmethod
  def get_location(cls):
    return cls.location

  @classmethod
  def read_config(cls, section, key):
    config = configparser.ConfigParser()
    config_file = "config.ini"
    config.read(config_file)
    return config[section][key]

  @abstractmethod
  def name(self):
    pass

  @abstractmethod
  def html_id(self):
    pass
  
  @abstractmethod
  def name_link(self):
    pass
  
  @abstractmethod
  def author(self):
    pass
  
  @abstractmethod
  def github_link(self):
    pass
  
  @abstractmethod
  def version(self):
    pass

  @abstractmethod
  def render_template(self):
    pass

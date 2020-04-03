from .plugin import Plugin
from plugins.jinja_adapter import Jinja_Adapter
from time import time
from .monitor import *

class Jinja(Jinja_Adapter):
    def __init__(self, Plugin):
        super().__init__(Plugin)

def start_jinja(Plugin):
    return Jinja(Plugin)
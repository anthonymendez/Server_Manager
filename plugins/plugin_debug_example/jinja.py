from .plugin import Plugin
from plugins.jinja_adapter import Jinja_Adapter
from time import time

class Jinja(Jinja_Adapter):

    @classmethod
    def timestamp_str(cls):
        return str(int(time()))

    @classmethod
    def custom_str(cls):
        return "I know right!?"

    def __init__(self, Plugin):
        super().__init__(Plugin)

def start_jinja(Plugin):
    return Jinja(Plugin)
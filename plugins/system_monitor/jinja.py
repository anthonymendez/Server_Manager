from .plugin import Plugin
from plugins.jinja_adapter import Jinja_Adapter
from time import time
from .monitor import *

class Jinja(Jinja_Adapter):

    @classmethod
    def cpu_count(cls):
        return cpu_count()

    @classmethod
    def cpu_percent_list(cls):
        return str(cpu_percent_list())

    @classmethod
    def cpu_stats(cls):
        return str(cpu_stats())

    @classmethod
    def mem_total(cls):
        return mem_total()

    @classmethod
    def mem_left(cls):
        return mem_left()

    def __init__(self, Plugin):
        super().__init__(Plugin)

def start_jinja(Plugin):
    return Jinja(Plugin)
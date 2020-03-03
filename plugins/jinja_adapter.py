from plugins.plugin_adapter import Plugin_Adapter
from abc import ABC, abstractmethod

class Jinja_Adapter(ABC):

    def name(self):
        return self.fn_name()

    def html_id(self):
        return self.fn_html_id()

    def name_link(self):
        return self.fn_name_link()

    def author(self):
        return self.fn_author()

    def github_link(self):
        return self.fn_github_link()

    def version(self):
        return self.fn_version()

    def render_template(self):
        return self.fn_render_template()

    @abstractmethod
    def __init__(self, Plugin_Adapter_inst):
        self.Plugin_Adapter_inst = Plugin_Adapter_inst
        self.fn_name = Plugin_Adapter_inst.name
        self.fn_html_id = Plugin_Adapter_inst.html_id
        self.fn_name_link = Plugin_Adapter_inst.name_link
        self.fn_author = Plugin_Adapter_inst.author
        self.fn_github_link = Plugin_Adapter_inst.github_link
        self.fn_version = Plugin_Adapter_inst.version
        self.fn_render_template = Plugin_Adapter_inst.render_template
        super().__init__()

class Jinja_Adapter:
    def __init__(self, fn_name, fn_html_id, fn_name_link, fn_author, fn_github_link, fn_version, fn_render_template):
        self.fn_name = fn_name
        self.fn_html_id = fn_html_id
        self.fn_name_link = fn_name_link
        self.fn_author = fn_author
        self.fn_github_link = fn_github_link
        self.fn_version = fn_version
        self.fn_render_template = fn_render_template

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
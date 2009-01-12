from paste.script.templates import Template
from paste.util.template import paste_script_template_renderer

class StapleSiteTemplate(Template):
    _template_dir = 'paster_template'
    summary = 'basic structure for a staple site'
    template_renderer = staticmethod(paste_script_template_renderer)

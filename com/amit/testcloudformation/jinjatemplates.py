import jinja2
import os


"""
 This file is used to setup a custom template in jinja2 which will automatically
 insert the contents of another template.
 Basic usage is:
 import jinjatemplates as myjinja
 myjinja.render("relativePath/To/File.template")

 Note: The jinja loader is set to search for templates from the cwd of the python interpeter
 or from the enviornment variable JINJA_TEMPLATE_PATH

"""

#private


def __include_file(name):
    return jinja2.Markup(__loader.get_source(__env, name)[0])

def _template_path():
    env_key = "JINJA_TEMPLATE_PATH"
    return os.environ.get(env_key, os.getcwd())

__loader = jinja2.FileSystemLoader(_template_path())
__env = jinja2.Environment(loader=__loader)
__env.globals['include_file'] = __include_file


#public

def render(template, context):
    print __env.list_templates()
    return __env.get_template(template).render(context)


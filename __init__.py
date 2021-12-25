from IPython.display import JSON, HTML, IFrame
from google.colab import output
from subprocess import getoutput
import os
import urllib.request

html_code_url = 'https://raw.githubusercontent.com/singhsidhukuldeep/Google-Colab-Shell/master/colab-shell.html'

def _run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


@_run_once
def __get_html_code(html_code_url=html_code_url):
    fp = urllib.request.urlopen(html_code_url)
    mybytes = fp.read()

    html_code = mybytes.decode("utf8")
    fp.close()
    return html_code

def __shell(command):
    if command.startswith('cd'):
        path = command.strip().split(maxsplit=1)[1]
        os.chdir(path)
        return JSON([''])
    return JSON([getoutput(command)])
output.register_callback('shell', __shell)

def getshell(height=450,html_code=__get_html_code()):
    html_code=html_code.replace('450',str(height))
    return HTML(html_code)

# !/usr/bin/env python3
# coding:utf-8
"""
Name       : __init__.py
Author     : Kuldeep Singh Sidhu
GitHub     : https://github.com/singhsidhukuldeep
Description: 
"""

from IPython.display import JSON, HTML, IFrame
from google.colab import output
from subprocess import getoutput
import os
import urllib.request

html_code_url = "https://raw.githubusercontent.com/singhsidhukuldeep/Google-Colab-Shell/master/html/colab-shell.html"


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
    if command.startswith("cd"):
        path = command.strip().split(maxsplit=1)[1]
        os.chdir(path)
        return JSON([""])
    return JSON([getoutput(command)])


output.register_callback("shell", __shell)


def getshell(height=400, html_code=__get_html_code()):
    """
    Displays a terminal for Google Colab. <3 Google

    Make sure this is the last command in the cell.

    Parameters
    ----------
    height : int, default 400
        height of the rendered terminal

    Returns
    -------
    IPython.display.HTML
        Displays the terminal

    Examples
    --------
    >>> getshell()

    >>> getshell(height=400)
    """

    html_code = html_code.replace("$$height$$", str(height))
    return HTML(html_code)

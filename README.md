<h1 align="center">Google Colab Shell </h1>

<p align="center">
  
  <a href="https://pypi.org/project/google-colab-shell/">
    <img src="https://github.com/singhsidhukuldeep/google-colab-shell/raw/main/img/colabshell.PNG" width="1080" alt="Go to https://pypi.org/project/google-colab-shell/">
  </a>
</p>

<p align="center">
<b>Free Terminals for everyone</b></b><br> Displays a terminal for Google Colab<br>
<a href="https://pypi.org/project/google-colab-shell/"><img src="https://img.shields.io/pypi/pyversions/google-colab-shell" alt="Go to https://pypi.org/project/google-colab-shell/"/></a>
<a href="https://pypi.org/project/google-colab-shell/"><img src="https://img.shields.io/pypi/v/google-colab-shell" alt="Go to https://pypi.org/project/google-colab-shell/"/></a>
<a href="https://pypi.org/project/google-colab-shell/"><img src="https://img.shields.io/pypi/status/google-colab-shell" alt="Go to https://pypi.org/project/google-colab-shell/"/></a>
<!-- <a href="https://pypi.org/project/google-colab-shell/"><img src="https://img.shields.io/pypi/format/google-colab-shell" alt="Go to https://pypi.org/project/google-colab-shell/"/></a> -->
<a href="https://lgtm.com/projects/g/singhsidhukuldeep/Google-Colab-Shell/context:javascript"><img alt="Language grade: JavaScript" src="https://img.shields.io/lgtm/grade/javascript/g/singhsidhukuldeep/Google-Colab-Shell.svg?logo=lgtm&logoWidth=18"/></a>
<a href="https://pypistats.org/packages/google-colab-shell"><img src="https://img.shields.io/pypi/dm/google-colab-shell"/></a>
<!-- <img src="https://visitor-badge.glitch.me/badge?page_id=request_boost" alt="Go to https://pypi.org/project/google-colab-shell/"/> -->
<img src="https://static.pepy.tech/personalized-badge/google-colab-shell?period=total&units=none&left_color=black&right_color=brightgreen&left_text=Total%20Downloads" alt="Go to https://pypi.org/project/google-colab-shell/"/>
</p>

## Setup

```shell
pip install google-colab-shell
```

## Usage

```python
# import the module once
from google_colab_shell import getshell
```

```python
## Anytime you awnt to open a terminal

getshell()

getshell(height=400) # custom height of the terminal
```
**IMPORTANT:** *Make sure `getshell` is the last command in the cell.*

## Documentation

```
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
```

## Credits

### Maintained by

***Kuldeep Singh Sidhu*** 

Github: [github/singhsidhukuldeep](https://github.com/singhsidhukuldeep)
`https://github.com/singhsidhukuldeep`

Website: [Kuldeep Singh Sidhu (Website)](http://kuldeepsinghsidhu.com)
`http://kuldeepsinghsidhu.com`

LinkedIn: [Kuldeep Singh Sidhu (LinkedIn)](https://www.linkedin.com/in/singhsidhukuldeep/)
`https://www.linkedin.com/in/singhsidhukuldeep/`

### Contributors

<a href="https://github.com/singhsidhukuldeep/google-colab-shell/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=singhsidhukuldeep/google-colab-shell" />
</a>

 The full list of all the contributors is available [here](https://github.com/singhsidhukuldeep/google-colab-shell/graphs/contributors)


[![https://github.com/singhsidhukuldeep](https://forthebadge.com/images/badges/built-with-love.svg)](http://kuldeepsinghsidhu.com)

#### TODO:: Want to contribute?

- [ ] Add streaming of the output to have wider range of uses
- [x] Detach the terminal to be async with other cells
- [ ] Set-up tests for edge cases and changes verification
- [ ] Set-up CI/CD pipleine (possibly using GitHub actions) to publish changes to PyPi
- [ ] Improeve the doc-strings documentation to add more explanantion and examples

## Say Thanks

 If this helped you in any way, it would be great if you could share it with others.

## Steps for publishing to `pypi` [This is just for me, Maybe!]

- `pip3 install setuptools twine`
- Go to project folder
- `python3 setup.py sdist`
- `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`

OR

Go to your project folder and:
```shell
pip3 install setuptools twine

python3 setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

## Current Status

[![Issues](https://img.shields.io/github/issues/singhsidhukuldeep/google-colab-shell)](https://github.com/singhsidhukuldeep/google-colab-shell/issues)
[![Contributors](https://badgen.net/github/contributors/singhsidhukuldeep/google-colab-shell)](https://github.com/singhsidhukuldeep/google-colab-shell/graphs/contributors)
[![Forks](https://badgen.net/github/forks/singhsidhukuldeep/google-colab-shell)](https://github.com/singhsidhukuldeep/google-colab-shell/network/members)
[![Stars](https://badgen.net/github/stars/singhsidhukuldeep/google-colab-shell)](https://github.com/singhsidhukuldeep/google-colab-shell/stargazers)
[![Watchers](https://badgen.net/github/watchers/singhsidhukuldeep/google-colab-shell)](https://github.com/singhsidhukuldeep/google-colab-shell/watchers)
[![Branches](https://badgen.net/github/branches/singhsidhukuldeep/google-colab-shell)](https://github.com/singhsidhukuldeep/google-colab-shell/branches)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python3.5+-1f425f.svg)](https://www.python.org/)
[![repo- size](https://img.shields.io/github/repo-size/singhsidhukuldeep/google-colab-shell)](https://github.com/singhsidhukuldeep/google-colab-shell)
[![Followers](https://img.shields.io/github/followers/singhsidhukuldeep?style=plastic&logo=github)](https://github.com/singhsidhukuldeep?tab=followers)

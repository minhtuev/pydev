Description
===========

`pydev` finds all python packages at specified path(s) and deploy
that packages in "[development mode](http://packages.python.org/distribute/setuptools.html#development-mode)".

So, packages deployed with `pydev` will be available for any Python module/script
and it source code will be at original paths.

Useful to use with [pyvcs](https://github.com/nickola/pyvcs).

Installation
============
    pip install -e git+https://github.com/nickola/pydev.git#egg=pydev

Usage
=====
    usage: pydev [-h] [--deps] [--scripts] path [path ...]

    Deploy Python packages in development mode.

    positional arguments:
      path        packages search path

    optional arguments:
      -h, --help  show this help message and exit
      --deps      install dependencies
      --scripts   install scripts

Example
=======
    mkdir components
    git clone https://github.com/django/django.git components/django
    hg clone https://bitbucket.org/mchaput/whoosh components/whoosh
    pydev components --deps --scripts

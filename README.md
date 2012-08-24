Description
===========

`pydev` find all python packages at specified path(s) and deploy
that packages in "[development mode](http://packages.python.org/distribute/setuptools.html#development-mode)".

Packages deployed with `pydev` will be available for any Python script and
their source code will be at original paths.

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
    git clone https://github.com/django/django.git django
    pydev django --deps --scripts

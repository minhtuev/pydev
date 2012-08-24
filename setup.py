#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='pydev',
      version='1.0',
      packages=find_packages(),
      entry_points={
          'console_scripts': ['pydev = pydev:execute_from_command_line'],
      }
)

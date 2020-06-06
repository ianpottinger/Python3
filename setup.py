#! /usr/bin/env python		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]

import keyword

DEBUG_MODE = True
if DEBUG_MODE:
    import pdb
    #pdb.set_trace()
    import logging
    FORMAT = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    logging.basicConfig(level = logging.INFO, format = FORMAT)
    #logging.basicConfig(level = logging.WARNING, format = FORMAT)
    #logging.basicConfig(level = logging.DEBUG, format = FORMAT)
    #logging.basicConfig(level = logging.ERROR, format = FORMAT)
    #logging.basicConfig(level = logging.CRITICAL, format = FORMAT)

RESERVED = ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
            'lambda', 'nonlocal', 'not', 'or', 'pass', 'print',
            'raise', 'return', 'try', 'while', 'with', 'yield']
KEYWORDS = keyword.kwlist

from setuptools import setup
import wheel


with open("README.md", "r") as markdown:
    overview = markdown.read()


setup (name = 'Py3onic',
       version = '1.3.5.7.9',
       description = 'Py3onic code',
       author = 'Potts',
       author_email = 'Potts@ian.org',
       url = "https://github.com/ianpottinger/Python3",
       packages = ['Py3onic'],
       package_dir = {'': 'src'},
       classifiers = [
           "Environment :: Win32 (MS Windows)",
           "Framework :: IDLE",
           "Framework :: IPython",
           "License :: Freeware",
           "License :: Free For Home Use",
           "License :: Free For Educational Use",
           "License :: OSI Approved :: MIT License",
           "License :: Public Domain",
           "Natural Language :: English",
           "Operating System :: Microsoft :: MS-DOS",
           "Operating System :: Microsoft :: Windows :: Windows XP",
           "Operating System :: Microsoft :: Windows :: Windows 7",
           "Operating System :: Microsoft :: Windows :: Windows 10",
           "Operating System :: OS Independent",
           "Programming Language :: Pascal",
           "Programming Language :: Python",
           "Programming Language :: Python :: 3.8",
           "Topic :: Software Development :: Libraries :: pygame"
           ],
       long_description = overview,
       long_description_content_type = "text/markdown",
       install_requires = [
           "maths ~= 1.3",
            ]
       )


"""
https://pypi.org/classifiers/
"""


"""
python3 setup.py sdist
python3 setup.py bdist_wheel sdist
python3 setup.py register
python3 setup.py sdist upload

pip3 install -e .
"""

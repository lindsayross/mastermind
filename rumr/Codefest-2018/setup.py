from setuptools import setu, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Rumr',
    version='0.0.0',
    description='Hello World',
    long_description=long_description,
    url='https://github.com/csandman/Codefest-2018',
    license='apache-2.0'
)

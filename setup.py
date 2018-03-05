from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyEX',
    version='0.0.6',
    description='Rest API to IEX',
    long_description=long_description,
    url='https://github.com/timkpaine/pyEX',
    download_url='https://github.com/timkpaine/pyEX/archive/v0.0.6.tar.gz',
    author='Tim Paine',
    author_email='timothy.k.paine@gmail.com',
    license='LGPL',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='finance data',
    packages=find_packages(exclude=[]),
)

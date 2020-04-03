from setuptools import setup, find_packages
from codecs import open
import io
import os
import os.path

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))
name = 'pyEX'


def get_version(file, name='__version__'):
    path = os.path.realpath(file)
    version_ns = {}
    with io.open(path, encoding="utf8") as f:
        exec(f.read(), {}, version_ns)
    return version_ns[name]

version = get_version(pjoin(here, name, '_version.py'))

with open(pjoin(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = [
    'deprecation>=2.0.6',
    'ipython>=7.2.0',
    'Pillow>=5.3.0',
    'pandas>=0.22',
    'pytz>=2019.1',
    'requests>=2.21.0',
    'socketIO-client-nexus>=0.7.6',
    'sseclient>=0.0.22',
    'temporal-cache>=0.1.1',
]

requires_dev = [
    'autopep8>=1.4.1',
    'bump2version>=1.0.0',
    'flake8>=3.7.8',
    'mock',
    'pytest>=4.3.0',
    'pytest-cov>=2.6.1',
    'Sphinx>=1.8.4',
    'sphinx-markdown-builder>=0.5.2',
] + requires

setup(
    name=name,
    version=version,
    description='Rest API to IEX',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/timkpaine/{name}'.format(name=name),
    author='Tim Paine',
    author_email='t.paine154@gmail.com',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='finance data',
    zip_safe=False,
    packages=find_packages(exclude=[]),
    install_requires=requires,
    extras_require={
        'dev': requires_dev,
    },
)

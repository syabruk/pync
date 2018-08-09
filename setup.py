#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

readme_file = os.path.join(here, 'README.md')
try:
    from m2r import parse_from_file
    long_description = parse_from_file(readme_file)
except ImportError:
    with codecs.open(readme_file, encoding='utf-8') as f:
        long_description = f.read()

terminal_notifier_files = []
for root, dirs, files in os.walk('pync/vendor/'):
    root = '/'.join(root.split('/')[1:])
    for f in files:
        terminal_notifier_files.append(os.path.join(root, f))

setup(name = 'pync',
    version = "2.0.4",
    description = 'Python Wrapper for Mac OS 10.10 Notification Center',
    long_description = long_description,
    author = 'Vladislav Syabruk',
    author_email = 'sjabrik@gmail.com',
    url = 'https://github.com/setem/pync',
    license = "MIT",
    platforms = "MacOS X",
    keywords = "mac notification center wrapper",
    zip_safe = True,
    include_package_data = True,
    install_requires = [
        'python-dateutil>=2.0'
    ],
    packages = find_packages(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Environment :: MacOS X',
        'Topic :: Terminals',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

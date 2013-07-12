#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

file_contents = []
for file_name in ('README.md',):
    path = os.path.join(os.path.dirname(__file__), file_name)
    file_contents.append(open(path).read())
long_description = '\n\n'.join(file_contents)

terminal_notifier_files = []
for root, dirs, files in os.walk('pync/vendor/'):
    root = '/'.join(root.split('/')[1:])
    for f in files:
        terminal_notifier_files.append(os.path.join(root, f))

package_data = {
    '': ['LICENSE', 'README.md'] + terminal_notifier_files,
}

setup(name = 'pync',
    version = "1.1",
    description = 'Python Wrapper for Mac OS 10.8 Notification Center',
    long_description = long_description,
    author = 'Vladislav Syabruk',
    author_email = 'sjabrik@gmail.com',
    url = 'https://github.com/setem/pync',
    download_url = 'https://github.com/downloads/setem/pync/pync-1.1.zip',
    license = "MIT",
    platforms = "MacOS X",
    keywords = "mac notification center wrapper",
    zip_safe = True,
    include_package_data = True,
    install_requires = [
        'python-dateutil>=2.0'
    ],
    package_data = package_data,
    packages = find_packages(),
    classifiers = [
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

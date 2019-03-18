from __future__ import unicode_literals

import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-Notifier',
    version=get_version('mopidy_notifier/__init__.py'),
    url='https://github.com/sauberfred/mopidy-notifier',
    license='Apache License, Version 2.0',
    author='sauberfred',
    author_email='florian.rott@me.com',
    description='Mopidy extension for displaying Trackinfo as notifications on Mac OS X 10.8 and Linux',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 0.18',
        'Pykka >= 1.1',
        'Pillow >= 4.1.0',
    ],
    entry_points={
        'mopidy.ext': [
            'notifier = mopidy_notifier:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)

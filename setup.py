#!/usr/bin/env python

import os
from setuptools import setup, find_packages

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name='MpsiSpider',
    version='0.0.1',
    description=(
        'A asyncchronous,multiprocessing spider famework'
    ),
    long_description=read('README.md'),
    author='Woe1997',
    author_email='413122031@qq.com',
    maintainer='Woe1997',
    maintainer_email='413122031@qq.com',
    license='MIT',
    packages=find_packages(),
    platforms=["all"],
    install_requires=['aiohttp'],
    url='https://github.com/daijiangtian/MpsiSpider',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    package_data={'MpsiSpider': ['utils/*.txt']}
)
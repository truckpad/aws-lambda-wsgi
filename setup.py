#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()


def version():
    git_version = None
    try:
        git_tag = subprocess.check_output(['git', 'describe', '--tags'])
        if git_tag:
            git_version = git_tag.strip()[1:]
            with open('VERSION', 'w') as version_file:
                version_file.write(git_version)
    except:
        pass
    if not git_version:
        try:
            with open('VERSION', 'r') as version_file:
                git_version = version_file.read()
        except:
            git_version = 'SNAPSHOT'
    return str(git_version)


setup(
    name='geo_api',
    version=version(),
    packages=['aws_lambda_wsgi'],
    description='AWS Lambda WSGI - ',
    long_description=read('README.md'),
    author='Marcos Araujo Sobrinho',
    author_email='marcos.sobrinho@truckpad.com.br',
    url='https://github.com/truckpad/aws-lambda-wsgi',
    install_requires=read('requirements.txt').strip().split('\n'),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP'
    ]
)

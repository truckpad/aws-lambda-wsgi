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
            git_version = git_tag.strip()[1:].decode('utf-8')
    except:
        pass
    if not git_version:
        git_version = 'SNAPSHOT'
    return git_version


setup(
    name='aws_lambda_wsgi',
    version=version(),
    packages=['aws_lambda_wsgi'],
    description='AWS Lambda WSGI - WSGI adapter for AWS API Gateway/Lambda Proxy Integration',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
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

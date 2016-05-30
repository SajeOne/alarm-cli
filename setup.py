#!/usr/bin/env python

from setuptools import setup

setup(name='alarmlib',
        version='0.1',
        description='Simple alarm app for the command line',
        url='https://github.com/SajeOne/alarm-cli',
        author='Shane "SajeOne" Brown',
        author_email='contact@shane-brown.ca',
        license='GPL3',
        zip_safe=False,
        package_dir={'alarm-cli': 'src'},
        packages=['alarm-cli'],
        scripts=['scripts/alarm-cli'])

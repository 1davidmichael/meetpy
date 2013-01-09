#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = 'meet',
	version = '0.0.1',
	author_email = '1.david.michael@gmail.com',
	packages = ['meet'],
	long_description=read('README.rst'),
	install_requires = [
		'paramiko',
	],
	entry_points = {
		'console_scripts':
			['meet = meet:run']
	}
)

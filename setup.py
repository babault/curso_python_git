#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from setuptools import setup

#def readme():
#    with open('README.org') as f:
#        return f.read()

setup(name='ex1',
      version='0.1', # antes version 0.4
      description='Operadores',
#      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='operadores con comandos',
#      scripts=['ex1/app/op'],
      url='http://github.com/babault//ex1',
      author='Julien Babault',
      author_email='julien.jbabault@gmail.com',
      license='GPLv3',
      packages=['ex1', 'ex1.app'],
      packages_dir={'ex1':'ex1', 'ex1.app':'ex1/app'},
      install_requires=[
          'markdown',
      ],
#      test_suite='nose.collector',
#      tests_require=['nose', 'nose-cover3'],
#      entry_points={
#          'console_scripts': ['funniest-joke=funniest.command_line:main'],
#    },
      include_package_data=True,
      zip_safe=False)

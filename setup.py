##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.app.schema package
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

ZCML_REQUIRE = [
    'zope.configuration',
    'zope.security',
]

TESTS_REQUIRE = [
    'zope.testing',
    'zope.testrunner',
] + ZCML_REQUIRE

setup(name='zope.app.schema',
      version='4.1.1.dev0',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      description='Component Architecture based Vocabulary Registry',
      long_description=(
          read('README.rst')
          + '\n\n' +
          read('src', 'zope', 'app', 'schema', 'README.rst')
          + '\n\n' +
          read('CHANGES.rst')
          ),
      keywords="zope3 vocabulary registry local component",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope :: 3',
      ],
      url='http://pypi.python.org/pypi/zope.app.schema',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      extras_require={
          'test': TESTS_REQUIRE,
          'zcml': ZCML_REQUIRE,
      },
      install_requires=[
          'setuptools',
          'zope.vocabularyregistry >= 1.0.0',
      ],
      include_package_data=True,
      tests_require=TESTS_REQUIRE,
      test_suite='zope.app.schema.tests.test_suite',
      zip_safe=False,
)

# Copyright (c) 2008-2013 Simplistix Ltd
# See license.txt for license details.

import os
from setuptools import setup

name = 'xlutils'
base_dir = os.path.dirname(__file__)

package_dir = os.path.join(os.path.dirname(__file__),'xlutils')

setup(
    name='suap-xlutils',
    version=open(os.path.join(base_dir, name, 'version.txt')).read().strip(),
    author='Chris Withers',
    author_email='chris@simplistix.co.uk',
    license='MIT',
    description="Utilities for working with Excel files that require both suap-xlrd and xlwt",
    long_description=open(os.path.join(base_dir, 'README.rst')).read(),
    url='http://www.python-excel.org',
    keywords="excel xls xlrd xlwt",
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['xlutils','xlutils.tests'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
    'suap-xlrd >= 1.1.1',
    'xlwt >= 0.7.4',
    ],
    entry_points = {
        'console_scripts': [
            'margins = xlutils.margins:main',
        ],
        },
    package_data={
        'xlutils': [
            '*.txt'
        ],
        'xlutils.tests': [
            '*.txt',
            '*.xls*'
        ],
    },
    extras_require=dict(
        test=[
            'errorhandler',
            'manuel',
            'mock',
            'nose',
            'nose-fixes',
            'nose-cov',
            'coveralls',
            'testfixtures',
            'tox',
        ],
        build=[
            'setuptools-git',
            'wheel',
            'twine',
            'sphinx',
            'pkginfo',
        ]

    )

)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as license_file:
    license = license_file.read()

requirements = [
    'Click'
]

test_requirements = []

setup(
    name='ioc_fanger',
    version='3.0.3',
    description="Python package to defang and refang indicators of compromise from text.",
    long_description=readme,
    author="Floyd Hightower",
    author_email='',
    url='https://github.com/ioc-fang/ioc_fanger',
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'fang=ioc_fanger.ioc_fanger:cli_fang',
            'defang=ioc_fanger.ioc_fanger:cli_defang'
        ]
    },
    include_package_data=True,
    package_data={'ioc_fanger': ['fang.json', 'defang.json']},
    install_requires=requirements,
    license=license,
    zip_safe=True,
    keywords='ioc_fanger',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

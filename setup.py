#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click',
]

test_requirements = []

setup(
    name='ioc_fanger',
    version='3.4.0',
    description="Python package to defang and fang indicators of compromise from text.",
    long_description=readme,
    long_description_content_type="text/markdown",
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
    license='MIT',
    zip_safe=True,
    project_urls={
        'Documentation': 'https://github.com/ioc-fang/ioc-fanger',
        'Say Thanks!': 'https://saythanks.io/to/floyd.hightower27%40gmail.com',
        'Source': 'https://github.com/ioc-fang/ioc-fanger',
        'Tracker': 'https://github.com/ioc-fang/ioc-fanger/issues',
        'PyPi': 'https://pypi.org/project/ioc-fanger/',
        'CI': 'https://travis-ci.com/ioc-fang/ioc-fanger.svg?branch=main',
        'Changelog': 'https://github.com/ioc-fang/ioc-fanger/blob/main/CHANGELOG.md',
    },
    keywords='iocs,indicators of compromise,threat intelligence,malware,threat hunting,observables,fanging,defanging,fang,defang,refang',
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

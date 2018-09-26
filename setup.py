#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0','six',
]

setup_requirements = [
    'pytest-runner>=2.11.1',
]

test_requirements = [
    'coverage>=4.5.1',
    'pytest>=3.4.2',
    'pytest-cov',
    'tox>=2.9.1',
]

development_requirements = [
    # general
    'bumpversion>=0.5.3',
    'pip>=9.0.1',
    'watchdog>=0.8.3',

    # docs
    'm2r>=0.2.0',
    'Sphinx>=1.7.1',
    'sphinx_rtd_theme>=0.2.4',

    # style check
    'flake8>=3.5.0',
    'isort>=4.3.4',

    # fix style issues
    'autoflake>=1.1',
    'autopep8>=1.3.5',

    # distribute on PyPI
    'twine>=1.10.0',
    'wheel>=0.30.0',
]

setup(
    author="Micah Smith",
    author_email='micahs@mit.edu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="This is a project in DAI Lab",
    entry_points={
        'console_scripts': [
            'project_dai=project_dai.cli:main',
        ],
    },
    extras_require={
        'test': test_requirements,
        'dev': development_requirements + test_requirements,
    },
    install_package_data=True,
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='project_dai',
    name='project_dai',
    packages=find_packages(include=['project_dai', 'project_dai.*']),
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/micahjsmith/project_dai',
    version='0.1.0',
    zip_safe=False,
)

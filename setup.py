import os
from pathlib import Path

from setuptools import find_packages, setup

long_description = os.path.join(Path(__file__).parent, 'README.md')

setup(
    name='universal_profanity',
    packages=find_packages(include=['universal_profanity']),
    version='0.1.1',
    description='Python library for text censoring in multiple languages.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='DillerDurak',
    author_email='isdedtool@gmail.com',
    maintainer='DillerDurak',
    maintainer_email='isdedtool@gmail.com',
    url='https://github.com/dillerdurak/universal-profanity',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.3'],
    test_suite='tests',
)

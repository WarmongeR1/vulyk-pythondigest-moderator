#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pip.req import parse_requirements

with open('README.rst') as readme_file:
    readme = readme_file.read()

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())

requirements = [str(ir.req) for ir in install_reqs]
test_requirements = requirements


setup(
    name='vulyk_pythondigest_moderator',
    version='0.1.0',
    description="Vulyk Pythondigest.ru moderator",
    long_description=readme,
    author="Alexander Sapronov",
    author_email='sapronov.alexander92@gmail.com',
    url='https://github.com/WarmongeR1/vulyk-pythondigest-moderator',
    packages=[
        'vulyk_pythondigest_moderator',
        'vulyk_pythondigest_moderator.models',
        'vulyk_pythondigest_moderator.static',
        'vulyk_pythondigest_moderator.views'
    ],
    package_dir={'vulyk_pythondigest_moderator':
                 'vulyk_pythondigest_moderator'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='vulyk_pythondigest_moderator',
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
    ],
)

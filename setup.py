#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    setup_requires=['setuptools_scm'],
    use_scm_version={'write_to': 'src/sphinx_autodoc_variants/_version.py'},
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)

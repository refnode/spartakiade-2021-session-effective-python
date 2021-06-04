#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.adoc") as fh_readme:
    readme = fh_readme.read()

install_reqs = []

setup(
    author="Sven Wilhelm",
    author_email='refnode@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description="Spartakiade 2021 Session Effective Python",
    install_requires=install_reqs,
    long_description=readme,
    include_package_data=True,
    keywords='spartakiade-2021-session-effective-python',
    name='spartakiade-2021-session-effective-python',
    packages=find_packages(where="src"),
    url='https://github.com/refnode/spartakiade-2021-session-effective-python',
    version='0.1.0',
    zip_safe=False,
)

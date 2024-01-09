# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from admin_styles import __version__

try:
    from pypandoc import convert
except ImportError:

    def convert(filename, fmt):
        with open(filename) as fd:
            return fd.read()


DESCRIPTION = "django admin styles"

CLASSIFIERS = [
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Development Status :: 3 - Alpha",
]


setup(
    name="django-admin-styles",
    version=__version__,
    author="Alaric Mägerle",
    author_email="info@rouxcode.ch",
    description=DESCRIPTION,
    long_description=convert("README.md", "rst"),
    url="https://github.com/rouxcode/django-admin-styles",
    license="MIT",
    keywords=["django"],
    platforms=["OS Independent"],
    classifiers=CLASSIFIERS,
    install_requires=[
        "django>=3.2",
    ],
    packages=find_packages(exclude=["example", "docs"]),
    include_package_data=True,
    zip_safe=False,
)

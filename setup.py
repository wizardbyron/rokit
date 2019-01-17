#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

about = {}

with open(os.path.join(here, "rokit", "__version__.py")) as f:
    exec(f.read(), about)

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel && twine upload dist/*")
    sys.exit()

setup(
    name = "rokit",
    packages = find_packages(),
    version=about["__version__"],
    description = "Redirection Optimization Kit",
    author = "wizardbyron",
    author_email = "wizard0530@gmail.com",
    url = "https://github.com/wizardbyron/rokit",
    keywords = ["url", "redirection", "redirect", "verify", "test", "tests"],
    classifiers = [
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities"
        ],
    install_requires=['requests'],
    entry_points={  
        'console_scripts':[ 
            'rokit = rokit.rokit:main'      
        ] 
    },
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    long_description = "rokit is a CLI tool for verifying and optimizing URLs redirection rules. It's easy to integrated with CI in smoke or regression test."
)
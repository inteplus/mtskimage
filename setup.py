#!/usr/bin/env python3

import os
from setuptools import setup, find_namespace_packages

setup(
    name="mtskimage",
    description="Minh-Tri Pham's extra modules for scikit-image",
    author=["Minh-Tri Pham"],
    packages=find_namespace_packages(include=["mt.*"]),
    # package_data={
    #    'skimagemt': ['*.pyx'],
    # },
    # include_package_data=True,
    # zip_safe=False,
    install_requires=[
        "scikit-image>=0.15.0",
        "mtgeo>=0.9.0",
    ],
    url="https://github.com/inteplus/mtskimage",
    project_urls={
        "Documentation": "https://mtdoc.readthedocs.io/en/latest/mt.skimage/mt.skimage.html",
        "Source Code": "https://github.com/inteplus/mtskimage",
    },
    setup_requires=["setuptools-git-versioning<2"],
    setuptools_git_versioning={
        "enabled": True,
        "version_file": VERSION_FILE,
        "count_commits_from_version_file": True,
        "template": "{tag}",
        "dev_template": "{tag}.dev{ccount}+{branch}",
        "dirty_template": "{tag}.post{ccount}",
    },
)

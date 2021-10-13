import sys
import os
import setuptools
import setuptools.command.build_py
import distutils.cmd
import distutils
from distutils.core import setup, Extension
import distutils.log
import distutils.log
distutils.log.set_verbosity(distutils.log.INFO)

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="solana_nfts", # Replace with your own username
    version="0.0.4",
    author="CryptomafiaGG",
    author_email="cryptomafiagg@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CryptomafiaGG/solana-nfts-python.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    keywords="solana nfts collections cryptocurrency api client",
)
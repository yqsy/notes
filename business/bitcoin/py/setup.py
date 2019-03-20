import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bitcoinhelper",
    version="0.0.1",
    author="yq",
    author_email="yqsy021@126.com",
    description=(""),
    license="BSD",
    packages=['bitcoinhelper', 'bitcoinhelper.impl'],
    entry_points="""
    [console_scripts]
    parseblockbtc = bitcoinhelper.parseblockbtc:main
    parseblockpkc = bitcoinhelper.parseblockpkc:main
    parseblockrsk = bitcoinhelper.parseblockrsk:main
    """
)

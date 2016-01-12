#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

def main():

    setuptools.setup(
        name             = "pyrecon",
        version          = "2016.01.12.1811",
        description      = "Python configuration reading",
        long_description = Markdown_to_reStructuredText("README.md"),
        url              = "https://github.com/wdbm/pyrecon",
        author           = "Will Breaden Madden",
        author_email     = "w.bm@cern.ch",
        license          = "GPLv3",
        py_modules       = ["pyrecon"],
        entry_points     = """
            [console_scripts]
            pyrecon = pyrecon:pyrecon
        """
    )

def read(*paths):
    with open(os.path.join(*paths), "r") as filename:
        return filename.read()

def Markdown_to_reStructuredText(filename):
    try:
        import pypandoc
        return pypandoc.convert(filename, "rst")
    except:
        print("pypandoc not found; long description could be corrupted")
        return read(filename)

if __name__ == "__main__":
    main()

# pyrecon

Python configuration reading

# introduction

Markdown lists are human-readable and machine-readable. So, they can be used to specify configurations written by humans for programs. This module features utilities for loading configurations specified in Markdown lists to Python dictionaries.

In order to facilitate the human-readability of configuration specifications, the idea is that lines that are not valid Markdown lists are ignored.

# quick start

Generally, pyrecon can be used in a way such as the following:

    # Import pyrecon.
    import pyrecon as pyrecon
    # Specify the configuration file.
    configurationFileName = "configuration.md"
    # Load the configuration specified in a configuration file to a Python dictionary.
    configuration = pyrecon.openConfiguration(configurationFileName)

The configuration dictionary then is usable with intelligence specified elsewhere in code.

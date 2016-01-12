#!/usr/bin/env python

import pyrecon

def main():

    print("\npyrecon examples\n")

    # Set the configuration file name.
    configuration_filename = "configuration.md"

    # The configuration file is opened and printed for the purposes of
    # illustration of the Markdown format of configuration.
    print("\nopen configuration file {filename}".format(
        filename = configuration_filename
    ))
    configuration_file = open(configuration_filename, "r").read()

    # The configuration file is directly opened and converted from the Markdown
    # format to a dictionary.
    print("\nconfiguration loaded and converted from Markdown list to dictionary:\n")
    configuration = pyrecon.open_configuration(configuration_filename)
    print(str(configuration) + "\n")

    # The configuration file is directly opened and converted from the Markdown
    # format to an ordered dictionary.
    print("\nconfiguration loaded and converted from Markdown list to ordered dictionary:\n")
    configuration = pyrecon.open_configuration(
        filename = configuration_filename
    )
    print(str(configuration) + "\n")

if __name__ == '__main__':
    main()

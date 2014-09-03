import pyrecon as pyrecon

def main():

    print("\npyrecon examples\n")

    # Set the configuration file name.
    configurationFileName = "configuration.md"

    # The configuration file is opened and printed for the purposes of
    # illustration of the Markdown format of configuration.
    configurationFile = open(configurationFileName, "r").read()
    print("\nopened configuration file:")
    print("\n" + configurationFile)

    # The configuration file is directly opened and converted from the Markdown
    # format to a dictionary.
    print("\nconfiguration loaded and converted from Markdown list to dictionary:\n")
    configuration = pyrecon.openConfiguration(configurationFileName)
    print(str(configuration) + "\n")

if __name__ == '__main__':

    main()

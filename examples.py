import pyrecon as pyrecon

def main():

    print("\npyrecon examples\n")
    configuration = open("configuration.md", "r").read()
    print("\nopened configuration file:")
    print("\n" + configuration)
    print("\nMarkdown list converted to dictionary:\n")
    print(str(pyrecon.MarkdownListToDictionary(configuration)) + "\n")

if __name__ == '__main__':

    main()

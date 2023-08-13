#!/usr/bin/python3

if __name__ == "__main__":
    "Print the number of arguments and list of arguments."
    from sys import argv

    argc = len(argv) - 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))

    for i in range(argc):
        print("{}: {}".format(i + 1, argv[i + 1]))

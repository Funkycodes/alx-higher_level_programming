#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    args = argv[1:]
    argv_length = len(args)
    if argv_length == 0:
        print("{:d} arguments.".format(argv_length))
    elif argv_length == 1:
        print("{:d} argument:".format(argv_length))
    else:
        print("{:d} arguments:".format(argv_length))

    argv_length = 1
    for arg in args:
        print("{:d}: {:s}".format(argv_length, arg))
        argv_length += 1

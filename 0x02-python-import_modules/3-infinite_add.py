#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    args_sum = 0
    for arg in argv[1:]:
        args_sum += int(arg)
    print("{:d}".format(args_sum))

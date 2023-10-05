#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv
    length = len(argv)
    if length == 1:
        print('{:d} arguments.'.format((length - 1)))
    if length == 2:
        print('{:d} argument:'.format((length - 1)))
        print('{:d}: {:s}'.format(length - 1, argv[length - 1]))
    if length > 2:
        print('{:d} arguments:'.format((length - 1)))
        for i in range(length, 1, -1):
            print('{:d}: {:s}'.format((length - i + 1), argv[length - i + 1]))

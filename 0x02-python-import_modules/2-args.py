#!/usr/bin/python3
import sys

length = len(sys.argv)
if length == 1:
    print('{:d} arguments.'.format((length - 1)))
if length == 2:
    print('{:d} argument:'.format((length - 1)))
    print('{:d}: {:s}'.format(length - 1, sys.argv[length - 1]))
if length > 2:
    print('{:d} arguments:'.format((length - 1)))
    for i in range(length, 1, -1):
        print('{:d}: {:s}'.format((length - i + 1), sys.argv[length - i + 1]))

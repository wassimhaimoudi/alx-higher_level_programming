#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) - 1 != 3:
        print('Usage: {:s} <a> <operator> <b>'.format(argv[0]))
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        print('Unknown operatorr. Available operators: +, -, * and /')
        exit(1)
    print('{:d} {:s} {:d} = {:d}'.format(a, op, b, result))

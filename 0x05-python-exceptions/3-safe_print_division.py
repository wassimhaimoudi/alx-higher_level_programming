#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        return (result)
    except Typeerror:
        pass
    finally:
        print('Inside result: {}'.format(result))
    return (result)

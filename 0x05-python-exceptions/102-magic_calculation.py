#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception("Too far")
            resullt += (a ** b) / i
        except Exception as e:
            print("Exception:", e)
            break
    result += a + b
    print(result)

#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, add, mul, div
    a = 10
    b = 5
    add_result = add(a, b)
    print("{} + {} = {}".format(a, b, add_result))
    sub_result = sub(a, b)
    print("{} - {} = {}".format(a, b, sub_result))
    mul_result = mul(a, b)
    print("{} * {} = {}".format(a, b, mul_result))
    div_result = div(a, b)
    print("{} / {} = {}".format(a, b, div_result))

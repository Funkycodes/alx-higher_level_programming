#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, mul, sub, div
    from sys import exit, argv

    def call_func(a, b, operator):
        if operator == "+":
            return add(a, b)
        elif operator == "-":
            return sub(a, b)
        elif operator == "*":
            return mul(a, b)
        else:
            return div(a, b)
    args = argv[1:]
    operators = "+ - * /".split()
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a, operator, b = args
        a = int(a)
        b = int(b)
        if operator in operators:
            print("{:d} {:s} {:d} = {:d}".format(
                a, operator, b, call_func(a, b, operator)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

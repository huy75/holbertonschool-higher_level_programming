#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    op = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in op:
        print("Unknown operator. Only: +, -, * and / available")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
    except:
        raise SystemExit("Input is not an integer")
    try:
        b = int(sys.argv[3])
    except:
        raise SystemExit("Input is not an integer")

    print("{:d} {} {:d} = {:d}".format(
        a, sys.argv[2], b, op[sys.argv[2]](a, b)))

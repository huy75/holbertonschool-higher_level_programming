#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    op = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    inOp = sys.argv[2]

    if inOp not in op:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)

    try:
        a = int(sys.argv[1])
    except:
        raise SystemExit("Input is not an integer")

    try:
        b = int(sys.argv[3])
    except:
        raise SystemExit("Input is not an integer")

    print("{} {} {} = {}".format(
        a, inOp, b, op[inOp](a, b)))

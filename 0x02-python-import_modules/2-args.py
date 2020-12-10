#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    n = len(args)
    print("{:d} argument{}{}"
          .format(n, "" if n == 1 else "s", "." if n == 0 else ":"))
    for i, arg in enumerate(args):
        print("{:d}: {}".format(i + 1, arg))

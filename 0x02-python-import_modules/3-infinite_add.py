#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    total = 0
    for each in args:
        try:
            total += int(each)
        except:
            raise SystemExit("Input is not an integer")
    print("{:d}".format(total))

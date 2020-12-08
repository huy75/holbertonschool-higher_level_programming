#!/usr/bin/python3
allBut = [ord('e'), ord('q')]
for i in range(ord('a'), ord('z')+1):
    if i in allBut:
        continue
    print("{:c}".format(i), end="")

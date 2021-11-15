#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""
import sys


if __name__ == "__main__":
    """ Code to retrieve and display datas"""
    size = 0
    statdict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def displaystat(size, statdict):
        """ function to print the stats"""
        print("File size: {}".format(size))
        for key, value in sorted(statdict.items()):
            if value != 0:
                print("{}: {}".format(key, value))

    nbline = 1
    try:
        """ Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> """
        for line in sys.stdin:
            try:
                linetok = line.split(" ")
                stat = int(linetok[-2])
                if stat in statdict:
                    statdict[stat] += 1
                    size += int(linetok[-1])
            except:
                pass

            if nbline % 10 == 0:
                displaystat(size, statdict)
            nbline += 1

    except KeyboardInterrupt:
        displaystat(size, statdict)
        raise
    displaystat(size, statdict)
    
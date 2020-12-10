#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for each in dir(hidden_4):
        if not each.startswith('__'):
            print(each)

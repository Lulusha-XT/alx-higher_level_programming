#!/usr/bin/python3
import sys


def main():
    a = len(sys.argv)
    if a == 1:
        print("0 arguments.")
    elif a == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(a - 1))
        for i in range(1, a):
            print("{:d}: {:s}".format(i, sys.argv[i]))

if __name__ == "__main__":
    main()

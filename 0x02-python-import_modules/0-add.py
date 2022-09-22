#!/usr/bin/python3
from add_0 import add


def main():
    a = 1
    b = 2
    print("{0:d} + {1:d} = {2:d}".format(a, b, add(a, b)))

if __name__ == "__main__":
    main()

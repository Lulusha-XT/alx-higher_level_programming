#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for items in matrix:
        for row in range(len(items)):
            print(
                "{:d}".format(items[row]),
                end="" if row == len(items) - 1 else " ")
        print()

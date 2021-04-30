#!/usr/bin/python3

import sys

def check_args():
    if (len(sys.argv) == 3):
        try:
            n = int(sys.argv[1])
            k = float(sys.argv[2])
            return (n, k)
        except ValueError:
            print("Wrong argument types")
            sys.exit(84)
    if (len(sys.argv) == 4):
        try:
            n = int(sys.argv[1])
            i0 = int(sys.argv[2])
            i1 = int(sys.argv[3])
            if (i0 >= i1):
                sys.exit(84)
            return (n, i0, i1)
        except ValueError:
            print("Wrong argument types")
            sys.exit(84)
    print("Wrong number of arguments")
    sys.exit(84)

# Calculates xi + 1 based on xi
def calc_next(xi, k):
    kxi = k * xi
    return kxi * ((1000 - xi) / 1000)

def individuals_x_generation(args):
    n = args[0]
    k = args[1]

    xi = n
    for i in range(1, 101):
        print("{} {:.2f}".format(i, xi))
        xi_next = calc_next(xi, k)
        xi = xi_next

def calc_gen_values(max_gen, min_gen, k, n_one):
    n = n_one
    i = 1
    x = []
    while (i < max_gen):
        n = k * n * ((1000 - n) / 1000)
        if (i >= min_gen):
            x.append(n)
        i += 1
    return (x)

def print_matrix_row(k, x_row):
    for value in x_row:
        print("{:.2f} {:.2f}".format(k, value))

def min_max_generation_growth(args):
    n = args[0]
    min_gen = args[1]
    max_gen = args[2]
    k = 1
    k_rep = 0

    matrix = [[0 for x in range(max_gen - min_gen +1)] for y in range(400)]
    while (k_rep <= 300):
        matrix[k_rep] = calc_gen_values(max_gen, min_gen, k, n)
        print_matrix_row(k, matrix[k_rep])
        k += 0.01
        k_rep += 1

def main():
    arguments = check_args()
    if (len(arguments) == 2):
        individuals_x_generation(arguments)
    if (len(arguments) == 3):
        min_max_generation_growth(arguments)

if __name__ == '__main__':
    main()
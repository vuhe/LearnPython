#!/usr/bin/env python3

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{} * {} = {:2}".format(j, i, j * i), end=' ')
    print('\n')

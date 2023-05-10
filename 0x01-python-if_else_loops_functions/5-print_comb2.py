#!/usr/bin/python3
for i in range(100):
    print("{i:2d}".format(i), end='')
    if i < 99:
        print(",", end='')

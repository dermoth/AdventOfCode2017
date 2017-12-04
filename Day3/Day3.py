#!/usr/bin/env python3

import math

# Given an array of height n:
# 1. For odd n, the distance from 1 for n**2 can be calculated
#    as (n/2, -n/2)
# 2. For even n, the distance from 2 for n**2 can be calculated
#    as (-n/2, n/2)
#100                         91
#    64 63 62 61 60 59 58 57
#    37 36 35 34 33 32 31 56
#    38 17 16 15 14 13 30 55
#    39 18  5  4  3 12 29 54
#    40 19  6  1  2 11 28 53
#    41 20  7  8  9 10 27 52
#    42 21 22 23 24 25 26 51
#    43 44 45 46 47 48 49 50
#109                      81 82

def dist(number):
    """Find the distance from 1 to number"""

    # Find the closest cartesian number to calculate distance from
    # We have two candidated around sqrt(number)
    low = int(math.sqrt(number))
    high = low + 1
    delta1 = abs(low ** 2 - number)
    delta2 = abs(high ** 2 - number)

    #print(number, low, high, delta1, delta2)

    if delta1 <= delta2:
        coord = getcoord(low, number)
    else:
        coord = getcoord(high, number)

    # Distance to origin is sum of absolute coordinates
    return abs(coord[0]) + abs(coord[1])

def getcoord(height, number):
    "Get coordinates for number with closest height"

    base = int(height / 2)
    # Calculate using height, but add one to get to the next edge
    # This simplifies calculating from higher number
    ref = height ** 2 + 1
    if height % 2:
        # Odd, and extend to the right
        coord = (base + 1, base * -1)
        if number > ref:
            # add delta to y
            coord = coord[0], coord[1] + number - ref
        elif number < ref:
            # subtract delta from x
            coord = coord[0] - ref + number, coord[1]
    else:
        # Even, and extend to the right (NB: from 2, so x + 1 - 1)
        coord = (base * -1, base)
        if number > ref:
            # subtract delta from y
            coord = coord[0], coord[1] - number + ref
        elif number < ref:
            # add delta to x
            coord = coord[0] + ref - number, coord[1]

    #print(number, height, ref, base, height, coord)
    return coord

#print(dist(1))
#print(dist(12))
#print(dist(23))
#print(dist(44))
#print(dist(99))
#print(dist(1024))
print(dist(325489))


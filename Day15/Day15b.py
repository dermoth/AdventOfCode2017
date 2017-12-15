#!/usr/bin/env python3

icnt = 5000000
#icnt = 5  # Test

count = 0
def genAgen():
    genAval = 699
    #genAval = 65  # Test

    for i in range(0, icnt):
        genAval = genAval * 16807 % 2147483647
        while genAval % 4 != 0:
            genAval = genAval * 16807 % 2147483647
        yield genAval

def genBgen():
    genBval = 124
    #genBval = 8921  # Test

    for i in range(0, icnt):
        genBval = genBval * 48271 % 2147483647
        while genBval % 8 != 0:
            genBval = genBval * 48271 % 2147483647
        yield genBval

for i, j in zip(genAgen(), genBgen()):
    #print(i, j)  # Test

    if (i & 0xFFFF) == (j & 0xFFFF):
        count += 1

print(count)


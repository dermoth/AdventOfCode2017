#!/usr/bin/env python3

genAval = 699
genBval = 124

# Test
#genAval = 65
#genBval = 8921

# Not used, see comment below
#genAfact = 16807
#genBfact = 48271
#genmodulo = 2147483647

count = 0
#for i in range(0, 5):  # Test
for i in range(0, 40000000):
    # ~20% speedup using constants here
    genAval = genAval * 16807 % 2147483647
    genBval = genBval * 48271 % 2147483647

    #print(genAval, genBval)  # Test

    if (genAval & 0xFFFF) == (genBval & 0xFFFF):
        count += 1

print(count)


#!/usr/bin/env python3

def knothash(buf):
    """Performs a knot hash of given data"""

    data = [ord(i) for i in buf]

    endseq = [17, 31, 73, 47, 23]
    data.extend(endseq)

    pos = 0
    skp = 0
    lst = list(range(0,256))
    llen = len(lst)
    for i in range(64):
        for length in data:
            # Triple list to wrap around freely
            tmp = lst + lst + lst
            side1 = tmp[pos:pos+length]
            side2 = tmp[pos+length:pos+llen]
            side1.reverse()
            # Double result list so we can get it with proper offset
            tmp = side1 + side2 + side1 + side2
            lst = tmp[pos:llen+pos]
            lst = tmp[llen-pos:2*llen-pos]
            pos += length + skp
            while pos >= llen:
                pos -= llen
            skp += 1

    res = bytes()
    for sli in [slice(i, i+16) for i in range(0, 256, 16)]:
        val = 0
        for i in lst[sli]:
            val ^= i
        res += bytes([val],)

    return(res)

# Some tests...
#import binascii
#print(binascii.b2a_hex(knothash('')).decode())  # becomes a2582a3a0e66e6e86e3812dcb672a272
#print(binascii.b2a_hex(knothash('AoC 2017')).decode())  # becomes 33efeb34ea91902bb2f59c9920caa6cd
#print(binascii.b2a_hex(knothash('1,2,3')).decode())  # becomes 3efbe78a8d82f29979031a4aa0b16a9d
#print(binascii.b2a_hex(knothash('1,2,4')).decode())  # becomes 63960835bcdc130f0b66d7ff4f6a5a8e

key = 'oundnydw'

#key = 'flqrgnkx'  # test...
#for i in range(0, 8):
#    khash = knothash('-'.join((key, str(i))))
#    for i in khash[0:1]:
#        row = bin(ord(khash[0:1]))[2:].rjust(8, '0')
#        print(row.replace('0', '.').replace('1', '#'), end='')
#    print()

count = 0
for i in range(0, 128):
    khash = knothash('-'.join((key, str(i))))
    for i in khash:
        row = bin(i)[2:].rjust(8, '0')
        count += row.count('1')

print(count)


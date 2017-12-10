#!/usr/bin/env python3

import binascii

lst = list(range(0,256))
pos = 0
skp = 0

endseq = [17, 31, 73, 47, 23]
with open('input.txt', 'r') as f:
    data = [ord(i) for i in f.readline().strip()]

#data = [ord(i) for i in ''] # becomes a2582a3a0e66e6e86e3812dcb672a272
#data = [ord(i) for i in 'AoC 2017'] # becomes 33efeb34ea91902bb2f59c9920caa6cd
#data = [ord(i) for i in '1,2,3'] # becomes 3efbe78a8d82f29979031a4aa0b16a9d
#data = [ord(i) for i in '1,2,4'] # becomes 63960835bcdc130f0b66d7ff4f6a5a8e

data.extend(endseq)

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

print(binascii.b2a_hex(res).decode())


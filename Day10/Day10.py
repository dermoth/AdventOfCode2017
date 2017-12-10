#!/usr/bin/env python3

lst = list(range(0,256))
pos = 0
skp = 0

with open('input.txt', 'r') as f:
    data = [int(i) for i in f.readline().split(',')]

#lst = [0, 1, 2, 3, 4]
#data = [3, 4, 1, 5]

llen = len(lst)
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
    if pos >= llen:
        pos -= llen
    skp += 1

print(lst[0] * lst[1])


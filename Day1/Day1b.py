#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = f.readline().strip()

#data = '12131415'

dlen = len(data)
prev = data[int(dlen/2)]
res = 0

for i in range(0, dlen):
    half = int(dlen/2 + i)
    if half >= dlen:
        half -= dlen
    if data[half] == data[i]:
        res += int(data[i])
    prev = data[half] 

print(res)


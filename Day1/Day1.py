#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = f.readline().strip()

#data = '91212129'

prev = data[-1]
res = 0
for l in data:
    if prev == l:
        res += int(l)
    prev = l

print(res)


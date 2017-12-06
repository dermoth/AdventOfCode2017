#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    banks = [int(i) for i in f.readline().split()]

#banks = [0, 2, 7, 0]

states = set()
firstloop = True

cnt = len(banks)
loop = 0
while True:
    loop += 1
    value = max(banks)
    idx = banks.index(value)
    banks[idx] = 0
    while value:
        idx += 1
        if idx >= cnt:
            idx -= cnt
        banks[idx] += 1
        value -= 1
    key = tuple(banks)
    if key in states:
        if firstloop:
            firstloop = False
            states = set()
            loop = 0
        else:
            break
    states.add(key)

print(loop)


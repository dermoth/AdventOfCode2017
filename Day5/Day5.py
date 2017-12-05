#!/usr/bin/env python3

data = []
with open('input.txt', 'r') as f:
    data.extend([int(i) for i in f])

#data = [0, 3, 0, 1, -3]

i = 0
count = 0
while True:
    count += 1
    step = data[i]
    data[i] += 1
    i += step
    if i >= len(data):
        break

print(count)


#!/usr/bin/env python3

data = []
with open('input.txt', 'r') as f:
    for line in f:
        data.append(line.split())

#data = [
#    ['5', '1', '9', '5'],
#    ['7', '5', '3'],
#    ['2', '4', '6', '8'],
#]

res = 0
for line in data:
    minv = int(line[0])
    maxv = int(line[0])
    for cell in line[1:]:
        val = int(cell)
        if minv > val:
            minv = val
        elif maxv < val:
            maxv = val
    res += maxv - minv
            
print(res)


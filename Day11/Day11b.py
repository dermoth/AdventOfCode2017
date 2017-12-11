#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = f.readline().strip().split(',')

# map hex grid into a x, y, z. x is West <-> East, then Y and Z going
# counter-clockwise like a cartesian map
dirmap = {
    'n':  ( 0,  1,  1),
    'ne': ( 1,  1,  0),
    'se': ( 1,  0, -1),
    's':  ( 0, -1, -1),
    'sw': (-1, -1,  0),
    'nw': (-1,  0,  1),
}

x = 0
y = 0
z = 0
res = 0
for i in data:
    xx, yy, zz = dirmap[i]
    x += xx
    y += yy
    z += zz
    res = max(res, abs(x), abs(y), abs(z))

print(res)


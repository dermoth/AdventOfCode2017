#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = f.readline().strip()

#data = '<>' # 0 characters.
#data = '<random characters>' # 17 characters.
#data = '<<<<>' # 3 characters.
#data = '<{!>}>' # 2 characters.
#data = '<!!>' # 0 characters.
#data = '<!!!>>' # 0 characters.
#data = '<{o"i!a,<{i<a>' # 10 characters.

res = 0
lvl = 0
garbage = False
escape = False
gcnt = 0
for c in data:
    if garbage:
        if escape:
            escape = False
        elif c == '!':
            escape = True
        elif c == '>':
            garbage = False
        else:
            gcnt += 1
    else:
        if c == '{':
            lvl += 1
            res += lvl
        elif c == '}':
            lvl -= 1
        elif c == '<':
            garbage = True

print(res)
print(gcnt)


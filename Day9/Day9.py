#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = f.readline().strip()

#data = '{}' # 1 characters.
#data = '{{{}}}' # 6 characters.
#data = '{{},{}}' # 5 characters.
#data = '{{{},{},{{}}}}' # 16 characters.
#data = '{<a>,<a>,<a>,<a>}' # 1 characters.
#data = '{{<ab>},{<ab>},{<ab>},{<ab>}}' # 9 characters.
#data = '{{<!!>},{<!!>},{<!!>},{<!!>}}' # 9 characters.
#data = '{{<a!>},{<a!>},{<a!>},{<ab>}}' # 3 characters.

res = 0
lvl = 0
garbage = False
escape = False
for c in data:
    if garbage:
        if escape:
            escape = False
        elif c == '!':
            escape = True
        elif c == '>':
            garbage = False
    else:
        if c == '{':
            lvl += 1
            res += lvl
        elif c == '}':
            lvl -= 1
        elif c == '<':
            garbage = True

print(res)


#!/usr/bin/env python3

import re
regex = re.compile(r'^(\w+)\s*\((\d+)\)(?:\s*->\s*((?:\w+, )*\w+))?\s*$')

weights = {}
prgmap = {}
revmap = {}
#with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for line in f:
        match = regex.match(line)
        if match:
            prgname, weight, childlst = match.groups()
            weights[prgname] = weight
            if childlst:
                children = childlst.split(', ')
                prgmap[prgname] = set(children)
                for i in children:
                    revmap[i] = prgname
        else:
            raise Exception('Line mismatch: ' + line)

first = None
for k in prgmap.keys():
    if k not in revmap:
        first = k

print(first)


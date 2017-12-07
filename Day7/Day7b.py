#!/usr/bin/env python3

import sys
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
            weights[prgname] = int(weight)
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
#print(first)

def checksum(name):
    if name in prgmap:
        csum = 0
        lsum = None
        othersums = []
        uweight = None
        oweight = None
        balance = set()
        for i in prgmap[name]:
            weight = checksum(i)
            if lsum is None:
                lsum = weight
                balance.add(i)
            elif weight == lsum:
                balance.add(i)
            else:
                othersums.append(weight)
            csum += weight
        imbalance = set(prgmap[name]).difference(balance)

        if imbalance:
            if len(othersums) > 1:
                bad, = balance
                good = imbalance.pop()
                outlier = lsum
                others = othersums[0]
            else:
                bad, = imbalance
                good = balance.pop()
                outlier = othersums[0]
                others = lsum
            goodw = weights[bad] - abs(others - outlier)
            print("%s is imbalanced: %i (should be %i)" % (bad, weights[bad], goodw))
            sys.exit(1)
        return weights[name] + csum
    return weights[name]

print(checksum(first))


#!/usr/bin/env python3

testdata = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
'''

groups = []
#for f in [[i for i in testdata.strip().split('\n')]]:
with open('input.txt', 'r') as f:
    for line in f:
        prog, sep, plist = line.split(None, 2)
        prog = int(prog)

        # Create a group
        group = set((prog,))

        # Add all other procs to it
        group.update([int(i) for i in plist.split(',')])

        # Find an intersection to merge with or add ourself
        found = False
        for grp in groups:
            if grp.intersection(group):
                grp.update(group)
                found = True
                break
        if not found:
            groups.append(group)

# Find intersections and group progs together
while True:
    length = len(groups)
    newgrps = [groups.pop()]
    while groups:
        grp = groups.pop()
        found = False
        for ngrp in newgrps:
            if ngrp.intersection(grp):
                ngrp.update(grp)
                found = True
        if not found:
            newgrps.append(grp)

    groups = newgrps
    if length == len(newgrps):
        break

# Finally, find group that contains 0 and count elements
for grp in groups:
    if 0 in grp:
        print(len(grp))


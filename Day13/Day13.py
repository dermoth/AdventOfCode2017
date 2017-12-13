#!/usr/bin/env python3

testdata = '''0: 3
1: 2
4: 4
6: 4
'''

depths = []
#for f in [[i + '\n' for i in testdata.strip().split('\n')]]:
with open('input.txt', 'r') as f:
    for line in f:
        depth, rng = [int(i) for i in line.split(':')]

        # fill in blanks 
        last = len(depths)
        for i in range(last, depth):
            depths.append(0)

        depths.append(rng)

# Initial scanner states (position, direction{True:fwd, False:rev}):
# NB: Dir at 0 always False, switches on next run
states = {i: (0, False) for i in range(0, len(depths)) if depths[i]}
severity = 0
for i in range(0, len(depths)):
    if i in states and states[i] == (0, False):
       severity += i * depths[i]

    # Advance states one ps
    for k, v in states.items():
        pos, fwd = v
        if pos == 0:
            fwd = True
        elif pos == depths[k] - 1:
            fwd = False
        if fwd:
            pos += 1
        else:
            pos -= 1
        states[k] = (pos, fwd)

print(severity)

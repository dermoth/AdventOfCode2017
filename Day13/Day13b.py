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
# scan each delay in parallel... Turns out to be very slow anyway, can
# be done much faster, ex:
# https://www.reddit.com/r/adventofcode/comments/7jgyrt/2017_day_13_solutions/dr6c89f/
caughtcnt = []
steps = len(depths)
i = 0
while True:
    caughtcnt.append(0)
    slen = len(caughtcnt)
    first = i - steps
    first = first if first >= 0 else 0

    for j in range(first, slen):
        depth = i - j
        pos = slen - depth - 1
        if depth in states and states[depth] == (0, False):
            #severities[pos] += depth * depths[depth]
            caughtcnt[pos] += 1

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

    i += 1
    if i > steps and caughtcnt[i-steps] == 0:
        print(i - steps)
        break


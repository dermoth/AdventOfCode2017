#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = f.readline().strip().split(',')

# Programs a to p
pgm = ''.join([chr(i) for i in range(ord('a'), ord('p')+1)])

# Functions
def exch(pgm, spec):
    tmp = [int(i) for i in spec.split('/')]
    tmp.sort()
    src, dst = tmp

    return pgm[:src] + pgm[dst] + pgm[src+1:dst] + pgm[src] + pgm[dst+1:] 

def part(pgm, spec):
    tmp = [pgm.index(i) for i in spec.split('/')]
    tmp.sort()
    src, dst = tmp

    return pgm[:src] + pgm[dst] + pgm[src+1:dst] + pgm[src] + pgm[dst+1:] 
    
func = {
    's': lambda x, y: x[int(y)*-1:] + x[:int(y)*-1],
    'x': exch,
    'p': part,
}

# Chances are over 1000000000 we'll get back to our origin position...
# See how many loops that is and skip them
opgm = pgm
cnt = 0
while True:
    for f in data:
        op = f[0]
        spec = f[1:]
        pgm = func[op](pgm, spec)
    cnt += 1
    if pgm == opgm:
        break

print('Got back to initial position after %i loops, skipping...' % cnt)
for _ in range(0, 1000000000 % cnt):
    for f in data:
        op = f[0]
        spec = f[1:]
        pgm = func[op](pgm, spec)

print(pgm)


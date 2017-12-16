#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    data = f.readline().strip().split(',')

#data = ['s1', 'x3/4', 'pe/b']  # test

# Programs a to p
pgm = ''.join([chr(i) for i in range(ord('a'), ord('p')+1)])
#pgm = 'abcde'  # test

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

for f in data:
    op = f[0]
    spec = f[1:]
    pgm = func[op](pgm, spec)

print(pgm)


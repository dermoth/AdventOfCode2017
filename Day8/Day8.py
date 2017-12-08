#!/usr/bin/env python3

# Engine
asm = {
    '==': lambda a, b: a == b,
    '>': lambda a, b: a > b,
    '>=': lambda a, b: a >= b,
    '<': lambda a, b: a < b,
    '<=': lambda a, b: a <= b,
    '!=': lambda a, b: a != b,
    'inc': lambda a, b: a + b,
    'dec': lambda a, b: a - b,
}

regs = {}
#with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for line in f:
        regA, op, incr, sep, regB, cond, val = line.split()
        rvB = regs.get(regB, 0)
        if asm[cond](rvB, int(val)):
            rvA = regs.get(regA, 0)
            regs[regA] = asm[op](rvA, int(incr))

print(max(regs.values()))


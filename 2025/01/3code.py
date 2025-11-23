#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

names = notes[0].strip().split(sep=',')
instructions = notes[2].split(sep=',')


for inst in instructions:
    if inst[0] == 'L':
        ptr = 0 - int(inst[1:])
        while ptr < 0: ptr += len(names)
    elif inst[0] == 'R':
        ptr = int(inst[1:])
        while ptr > len(names) - 1: ptr -= len(names)
    else:
        raise ValueError("What the fuck")

    xchg = names[0]
    names[0] = names[ptr]
    names[ptr] = xchg


print(names[0])
pass
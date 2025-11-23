#!/usr/bin/env python3

import os

with open("./2025/01/1notes", 'r') as infile:
    notes = infile.readlines()

names = notes[0].strip().split(sep=',')
instructions = notes[2].split(sep=',')

left = 0
right = len(names) - 1
ptr = 0


for inst in instructions:
    if inst[0] == 'L':
        ptr -= int(inst[1])
        if ptr < left: ptr = left
    elif inst[0] == 'R':
        ptr += int(inst[1])
        if ptr > right: ptr = right
    else:
        raise ValueError("What the fuck")

print(names[ptr])
pass

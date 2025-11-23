#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

names = notes[0].strip().split(sep=',')
instructions = notes[2].split(sep=',')

left = 0
right = len(names) - 1
ptr = 0

def normalise(num, len):
    while num not in range(len):
        if num < 0:
            num += len
        if num > len - 1:
            num -= len
    return num

for inst in instructions:
    if inst[0] == 'L':
        ptr -= int(inst[1:])
        ptr = normalise(ptr, len(names))
    elif inst[0] == 'R':
        ptr += int(inst[1:])
        ptr = normalise(ptr, len(names))
    else:
        raise ValueError("What the fuck")

print(names[ptr])
pass
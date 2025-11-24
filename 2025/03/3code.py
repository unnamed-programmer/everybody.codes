#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

crates = []
for i in notes[0].split(','): crates.append(int(i))
crates.sort()

stacks = []
stacks.append(crates)
stacks.append([])
duplicates = True
depth = 0
while duplicates:
    stacks[depth].sort()
    stacks.append([])
    duplicates = False
    for i in stacks[depth]:
        while stacks[depth].count(i) > 1:
            stacks[depth + 1].append(stacks[depth].pop(stacks[depth].index(i)))
            duplicates = True
    depth += 1
    


print(len(stacks) - 1)
pass
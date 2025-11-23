#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

crates = []
for i in notes[0].split(','): crates.append(int(i))
crates.sort()

for i in crates:
    while crates.count(i) > 1:
        crates.pop(crates.index(i))

print(sum(i for i in crates))
pass
#!/usr/bin/env python3

import os
import math

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

gears = []
gears.append([0, int(notes[0].strip())])
for i in range(1, len(notes) - 1):
    gears.append([int(x) for x in notes[i].strip().split('|')])
gears.append([int(notes[-1].strip()), 0])


turns = 100


for i in range(1, len(gears)):
    turns *= (gears[i - 1][1] / gears[i][0])
    pass

turns = math.floor(turns)


print(turns)
pass
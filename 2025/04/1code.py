#!/usr/bin/env python3

import os
import math

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

gears = [int(i.strip()) for i in notes]

turns = 2025

for i in range(1, len(gears)):
    turns *= (gears[i - 1] / gears[i])
    pass

turns = math.floor(turns)
print(turns)
pass
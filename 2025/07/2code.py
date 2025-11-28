#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

names = notes[0].strip().split(',')

strRules = [n.strip('\n') for n in notes[2:]]
rules = {}

for sr in strRules:
    sb, se = sr.split('>')
    sb = sb.strip(' ')

    if ',' in se:
        se = tuple(sei.strip(' ') for sei in se.split(','))
    else:
        se = tuple(se.strip(' '))

    rules[sb] = se

total = 0
for n in range(len(names)):
    name = names[n]
    acc = True
    for i in range(len(name) - 1):
        if name[i + 1] not in rules[name[i]]:
            acc = False
            continue
    if acc: 
        total += n + 1

print(total)
pass
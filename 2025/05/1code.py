#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

ident, segs = notes[0].split(':')

ident = int(ident)
segs = [int(x) for x in segs.split(',')]

sword = []
sword.append([None, None, None])
layer = 0

for s in segs:
    if all(sword[layer][n] != None for n in [0, 1, 2]):
        layer += 1
        if len(sword) < layer + 1: sword.append([None, None, None])

    cl = layer
    while True:
        if sword[cl][1] == None:
            sword[cl][1] = s
            break
        elif s < sword[cl][1] and sword[cl][0] == None:
            sword[cl][0] = s
            break
        elif s > sword[cl][1] and sword[cl][2] == None:
            sword[cl][2] = s
            break
        else:
            cl += 1
            if len(sword) < cl + 1: 
                sword.append([None, None, None])

    pass

qualstr = ""
for l in sword:
    qualstr += str(l[1])

quality = int(qualstr)

print(quality)

pass

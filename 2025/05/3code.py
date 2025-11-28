#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

ident, segs = notes[0].split(':')

swords = dict()

for ln in notes:
    ident, segs = ln.split(':')
    ident = int(ident)
    segs = [int(x) for x in segs.split(',')]
    swords[ident] = segs

qualities = dict()

for ident, segs in swords.items():

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

    qualstr = ""
    for l in sword:
        qualstr += str(l[1])

    quality = int(qualstr)

    lscores = []
    for l in sword:
        l0 = str(l[0]) if l[0] is not None else ''
        l1 = str(l[1]) if l[1] is not None else ''
        l2 = str(l[2]) if l[2] is not None else ''
        lscores.append(int(f'{l0}{l1}{l2}'))

    score = f'{quality:20d}'
    for l in lscores:
        score += f'{l:05d}'
    score += f'{ident:03d}'

    qualities[ident] = int(score)

unsorted = [(k, v) for k, v in qualities.items()]
sortedList = sorted(unsorted, key=lambda x: x[1])[::-1]

csum = 0

for i in range(len(sortedList)):
    csum += (i + 1) * sortedList[i][0]

print(csum)
pass

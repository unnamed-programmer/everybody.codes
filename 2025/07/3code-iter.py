#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

ins = notes[0].strip().split(',')

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

lMin = 7
lMax = 11

total = 0

names = []

for name in ins:
    acc = True
    for i in range(len(name) - 1):
        if name[i] not in rules.keys():
            acc = False
            continue
        if name[i + 1] not in rules[name[i]]:
            acc = False
            continue
    if acc: 
        names.append(name)

results = []
inters = []
done = []

for name in names:
    out = []
    done.append(name)
    for l in rules[name[-1]]:
        out.append(name + l)
    for o in out:
        if len(o) < lMin:
            if o not in inters and o not in done: inters.append(o)
        elif len(o) <= lMax:
            if o not in inters and o not in done: inters.append(o)
            if o not in results: results.append(o)
    if name in inters: del inters[inters.index(name)]

cycles = 0

while len(inters) > 0:
    name = inters.pop(0)

    cycles += 1

    print(f'Cycle {cycles}: {len(results)} results, {len(inters)} to process, {len(done)} exhausted, {len(out)} processed last cycle - {name} at {len(name)}')

    if name not in done and name[-1] in rules.keys():

        done.append(name)

        for l in rules[name[-1]]:
            o = name + l

            if len(o) <= lMax:
                inters.append(o)
                if len(o) > lMin and name not in results:
                    results.append(o)



        

print(len(results))
pass
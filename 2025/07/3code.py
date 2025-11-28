#!/usr/bin/env python3

import os
import functools

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

results = set()

@functools.cache
def proc(name):
    global results
    global rules
    global lMin
    global lMax

    print(f'{len(results)} {name}')

    if name[-1] in rules.keys() and len(name) < lMax:
        
        for l in rules[name[-1]]:
            
            if len(name + l) >= lMin:
                results.add(name + l)

            proc(name + l)

for n in names: 
    proc(n)


        

print(len(results))
pass
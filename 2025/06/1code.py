#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()
    
people = [p for p in notes[0].strip()]

novices = []
for i in range(len(people)):
    if people[i] == 'a':
        novices.append(i)

mentors = []
for i in range(len(people)):
    if people[i] == 'A':
        mentors.append(i)

comboCount = 0
for novice in novices:
    for mentor in mentors:
        if mentor < novice:
            comboCount += 1

print(comboCount)


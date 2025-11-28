#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()
    
people = [p for p in notes[0].strip()]

comboCount = 0

for job in ['a', 'b', 'c']:

    novices = []
    for i in range(len(people)):
        if people[i] == job:
            novices.append(i)

    mentors = []
    for i in range(len(people)):
        if people[i] == job.upper():
            mentors.append(i)

    for novice in novices:
        for mentor in mentors:
            if mentor < novice:
                comboCount += 1

print(comboCount)


#!/usr/bin/env python3

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()
    
people = notes[0].strip()

bound = len(people)

people = people * 1000

distLimit = 1000

comboCount = 0

for job in ['a', 'b', 'c']:

    novices = []
    for i in range(len(people)):
        if people[i] == job:
            novices.append(i)

    for novice in novices:
        print(f'{novice:,} of {len(people):,} {job}')
        comboCount += people[max(0, novice - 1000):min(len(people), novice + 1001)].count(job.upper())
        #for i in range(max(0, novice - 1000), min(len(people), novice + 1001)):
        #    if people[i] == job.upper():
        #        comboCount += 1

  

print(comboCount)


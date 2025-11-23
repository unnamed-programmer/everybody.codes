#!/usr/bin/env python3

import math

import os

_filename = __file__.replace('code.py', 'notes')

with open(_filename, 'r') as infile:
    notes = infile.readlines()

class Complex:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return (f"Complex({self.x}, {self.y})")
    
    def __str__(self):
        return f"[{self.x},{self.y}]"

    def __getitem__(self, i):
        match i:
            case 0:
                return self.x
            case 1:
                return self.y
            case _:
                raise IndexError("Complex only has 2 items")

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("oh fuck")

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex((self.x * other.x) - (self.y * other.y), (self.x * other.y) + (self.y * other.x))
        else:
            raise TypeError("oh dear")

    def __floordiv__(self, other):
        if isinstance(other, Complex):
            return Complex(math.trunc(self.x / other.x), math.trunc(self.y / other.y))
        else:
            raise TypeError("oh god")


vals = notes[0].split('[')[1].split(']')[0].split(',')
A = Complex(int(vals[0]), int(vals[1]))
F = A + Complex(1000, 1000)

points = 0

for y in range(A.y, F.y + 1, 1):
    for x in range(A.x, F.x + 1, 1):
        print(f'\n{x}, {y}')

        res = Complex(0, 0)
        failed = False

        for i in range(1, 101):
            res = res * res
            res = res // Complex(100000, 100000)
            res = res + Complex(x, y)

            if res.x < -1000000 or res.x > 1000000 or res.y < -1000000 or res.y > 1000000:
                print(f'NO! {res}')
                failed = True
                break
        
        match [x, y]:
            case [35630,-64880]:
                assert failed == False
                # assert res is Complex(-2520, -5355)
            case [35630,-64870]:
                assert failed == False
                # assert res is Complex(5021, 6465)
            case [35640,-64860]:
                assert failed == False
                # assert res is Complex(-3291, -684)
            case [36230,-64270]:
                assert failed == False
                # assert res is Complex(-7266, 3234)
            case [36250,-64270]:
                assert failed == False
                # assert res is Complex(162903, -679762)
            case [35460, -64910]:
                assert failed == True
                assert i == 27
                # assert res is Complex(1265017, 932533)
            case [35470, -64910]:
                assert failed == True
                assert i == 28
                # assert res is Complex(-1724836, 19302)
            case [35480, -64910]:
                assert failed == True
                assert i == 30
                # assert res is Complex(-575306, 8705296)
            case [35680, -64850]:
                assert failed == True
                assert i == 95
                # assert res is Complex(-7919169, 5303832)
            case [35630, -64830]:
                assert failed == True
                assert i == 100
                # assert res is Complex(-6387697, -1621945)
            case _:
                pass

        if not failed:
            points += 1
            print('yes')


print(points)
pass
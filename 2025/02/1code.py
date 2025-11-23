#!/usr/bin/env python3

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
            return Complex(self.x // other.x, self.y // other.y)
        else:
            raise TypeError("oh god")


vals = notes[0].split('[')[1].split(']')[0].split(',')
A = Complex(int(vals[0]), int(vals[1]))

res = Complex(0, 0)

for _ in range(3):
    res = res * res
    res = res // Complex(10, 10)
    res = res + A

print(res)
pass
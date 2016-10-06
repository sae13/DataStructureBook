#!/bin/python
from os import system
system('clear')
def aTevanB(a, b):
    if b == 1:
        return a
    else:
        return aTevanB(a, (b - 1)) * a


def aMolb(a, b):
    if b == 1:
        return a
    else:
        return aMolb(a, (b - 1)) + a


print(aTevanB(2, 4))
print(aMolb(2, 8))
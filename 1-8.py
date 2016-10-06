#!/bin/python
from os import system
system('clear')
def gcd(x, y):
    if (y <= x) and (int(x)%int(y) == 0):
        return y
    elif (x<y):
        return gcd(y,x)
    else:
        return gcd(y, int(x)%int(y))
print(gcd(25,10))
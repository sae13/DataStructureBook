#!/bin/python
from os import system
system('clear')
def combination(n,m):
    if (m == 0) or (m == n):
        return 1
    else:
        return  combination(int(n)-1, m) + combination(int(n)-1, int(m)-1)
print(combination(15,13))
#!/bin/python
from os import system
system ('clear')
def threeDivisible (numm):
    listDivisibles=[]
    for i in range (1,numm):
        if (i%3==0):
            listDivisibles.append(i)
    return listDivisibles
print(threeDivisible(10))
def testsomething(nummm):
    threeDivisible2=[]
    if (nummm<=5):
       return 3
       print(3)
    else:
        return testsomething(int(nummm)-3)+3
        print(testsomething(int(nummm)-3)+3)
        
testsomething(104)

#!/bin/python
from os import system
system('clear')
print("Rescusive mode\n")
nlist=[]
nums=input("how much nums u have?")
for i in range (0,int(nums)):
    nlist.append(input("please enter your {}th number: ".format(int(i)+1)))       
print(nlist)
def sum(m):
    if (m==1):
        return int(nlist[0])
    else:
        return sum(int(m)-1)+int(nlist[int(m)-1])
print(sum(int(nums)))
print("non rescusive mode: \n")
nums=None
nums=input("how much nums u have?")
summ=0
for i in range (0,int(nums)):
    summ=int(summ)+int(input("whats your {}th number?".format(int(i)+1)))
print(summ)

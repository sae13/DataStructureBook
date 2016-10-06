#!/bin/python
from os import system
system('clear')
array = input("please enter a array: ")
def chapAzAkhar(str):
    arz = len(str)
    if arz==1:
        return str[0]
    else:
        return str[-1]+chapAzAkhar(str[:-1])

print(chapAzAkhar(array))
#!/bin/python
from os import system

system('clear')
# Reclusive Mode
number = str(input("Please enter your number: "))


def charINnewline(str):
    if str[0] == '0':
        str = str[1:]
    arz = len(str)
    if arz == 1:
        return str + '\n'
    else:
        return str[0] + '\n' + charINnewline(str[1:])


print(charINnewline(number))

# No Reclusive Mode
if number[0] == '0':
    number = number[1:]
for i in range(0, len(number)):
    print(number[i], end="\n")

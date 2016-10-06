#!/bin/python
from os import system

system('clear')
# Fib No Recessive
nTh =int(input("what is the number of fibonacci serie you want to know?"))
if (nTh == 1) or (nTh == 2):
    fibo = 1

fibo1 = fibo2 = 1
n = nTh - 2
fibo = None
for i in range(0, n):
    fibo = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo

print(fibo)

# Recessive mode
def fib(num):
    if (num == 1) or (num == 2):
        return 1
    else:
        return int(fib(int(num)-2) + fib(int(num) - 1))
print(fib(nTh))
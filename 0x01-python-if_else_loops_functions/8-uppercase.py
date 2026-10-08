#!/bin/env python
# uppercase=input("best")
# n=input("Best School 98 Battery street")
# for i in n:
#    n=chr(ord(i)-32)
#    print(n,end="")
def upper(n):
    for i in n:
        n= chr(ord(i)-32)
        print(n, end='')
# print(n, end='')
number= 98
upper("best")
# number= 98
upper("best school 98 battery street")
# upper("best", "best school 98 battery street", sep="\n")
# ("best school [number] battery street")

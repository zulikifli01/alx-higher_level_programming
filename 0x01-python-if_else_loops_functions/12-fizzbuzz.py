#!/bin/env python
''' def fizzbuzz():
    return (1, 101)
fizzbuzz()
print("")
for i in range(1, 101):
    print(i, end=" ") '''
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
fizzbuzz()

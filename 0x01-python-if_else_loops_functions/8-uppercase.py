#!/bin/env python
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print(f"{c}", end="")
    print("")
uppercase("best")
uppercase("Best School 98 Battery street")

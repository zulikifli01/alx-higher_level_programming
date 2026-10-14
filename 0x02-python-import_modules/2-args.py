#!/bin/env python
import sys
print(" arguments : ", len(sys.argv))
for i in range(1, len(sys.argv)):
    print(f"{i}: {sys.argv[i]}")
#    print(sys.argv[i])

#!/bin/env python
import sys
SUM=0
for i in range(1, len(sys.argv)):
    SUM+=int(sys.argv[i])
print(SUM)

#!/usr/bin/python3
import sys
if __name__ == "__main__":
    print(" arguments : ", len(sys.argv))
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
#    print(sys.argv[i])

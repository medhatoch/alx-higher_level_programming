#!/usr/bin/python3
import sys

argv = sys.argv[1:]
result = 0

for arg in argv:
    result += int(arg)

print(result)

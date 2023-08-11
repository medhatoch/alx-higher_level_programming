#!/usr/bin/python3.8
import hidden_4
import sys

def main():
    names = dir(hidden_4)
    
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    main()

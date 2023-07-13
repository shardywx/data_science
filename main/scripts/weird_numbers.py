import math
import os
import random
import re
import sys

def print_weird(number: int):
    """
    Problem taken from this site: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
    """
    if number % 2 == 1:
        print("Weird")
    else:
        if number >= 2 and number <= 5:
            print("Not Weird")
        elif number >= 6 and number <= 20:
            print("Weird")
        else:
            print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    print_weird(n)

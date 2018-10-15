#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    valley_count = 0

    for i in s:
        if i is "D":
            level -= 1
            
        elif i is "U":
            level += 1
            if level == 0:
                valley_count += 1
        else:
            pass
    
    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()


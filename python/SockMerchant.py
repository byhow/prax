#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    occ, occ_map = 0, dict()
    for i in ar:
        if i in occ_map:
            occ_map[i] += 1
            if occ_map[i] % 2 == 0:
                occ += 1
        else:
            occ_map[i] = 1

    return occ
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count, cmap, pairs = 0, {}, {}
    for i in reversed(arr):
        if i * r in pairs:
            count += pairs[i * r]
        if i * r in cmap:
            pairs[i] = pairs.get(i, 0) + cmap[i * r]

        cmap[i] = cmap.get(i, 0) + 1
    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + "\n")

    fptr.close()

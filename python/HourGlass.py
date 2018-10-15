#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    print(arr)
    min_score = - sys.maxsize - 1
    for i in range(0, 4):
        for j in range(0, 4):
            sum_val = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] 
            + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1]
            + arr[i + 2][j + 2]
            print("test index is " + str(arr[i + 1][j + 1]))
            print("At " + str(i) + " and " + str(j) + " val is " + str(sum_val))
            if sum_val > min_score:
                min_score = sum_val
    return min_score

if __name__ == '__main__':
    l = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    print(hourglassSum(l))


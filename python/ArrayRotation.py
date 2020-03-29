#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[(d % len(a)):] + a[:(d % len(a))]

if __name__ == '__main__':
    print(rotLeft([1, 2, 3,4, 5], 4))
 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    ans = 0
    for i,j in enumerate(q):
        if j - i > 3:
            print("Too chaotic")
            return
        for k in range(max(j - 2, 0), i):
            if q[k] > j:
                ans += 1
    print(ans)



if __name__ == '__main__':
    # t = int(input())

    # for t_itr in range(t):
    #     n = int(input())

    #     q = list(map(int, input().rstrip().split()))

    #     minimumBribes(q)
    minimumBribes([1 ,2, 5, 3, 7, 8, 6, 4])

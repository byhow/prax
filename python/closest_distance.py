# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys
def solution(stores, houses):
    # write your code in Python 3.6
    lToS = dict()

    for i in range(len(houses)):
        key = 0
        value = sys.maxsize
        lToS[i] = [key, value]
        # print("i is " + str(i))
        for j in range(len(stores)):
            distance = abs(stores[j] - houses[i])
            if distance < lToS[i][1]:
                lToS[i][0] = stores[j]
                lToS[i][1] = distance

    ret = []
    for (k, v) in lToS.items():
        ret.append(v[0])
    return ret

print(solution([1, 5, 20, 11, 16], [5, 10, 17]))
# [5, 11, 16]

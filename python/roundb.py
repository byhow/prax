import math


def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    ret = []
    for p in range(2, n):
        if prime[p]:
            ret.append(p)
    return ret


def prd(num):
    if num < 9:
        return 6
    N = math.ceil(((num + 1) ** 0.5) * 1.5)
    pNums = sieve(N)
    prd = 0
    # print(pNums)
    N = len(pNums)
    for i in range(1, N):
        # print(i)
        if pNums[i] * pNums[i - 1] > num:
            return prd
        else:
            prd = pNums[i] * pNums[i - 1]
    return prd


T = int(input())
for x in range(1, T + 1):
    print("Case #{}: {}".format(x, prd(int(input()))), flush=True)

# T = int(input())
# for x in range(1, T + 1):
#     N = int(input())
#     S = list(input())
#     tail = [0] * N
#     tail[0] = 1
#     for c in range(1, N):
#         if S[c] > S[c - 1]:
#             tail[c] = tail[c - 1] + 1
#         else:
#             tail[c] = 1

#     print("Case #{}: {}".format(x, " ".join(str(i) for i in tail)), flush=True)


# import math as m

# T = int(input())
# for x in range(1, T + 1):
#     N = int(input())
#     S = list(map(int, input().split()))
#     d = [0] * N
#     res = 0
#     for i in range(1, N):
#         d[i] = S[i] - S[i - 1]

#     comd = max(set(d), key=d.count)
#     maxd = [1] * N
#     idx = 1
#     flag = 2
#     while idx < N - 1:
#         if d[idx] == comd:
#             maxd[idx] += maxd[idx - 1]
#         else:
#             if flag > 0 and d[idx] + d[idx + 1] == comd:
#                 maxd[idx] += maxd[idx - 1]
#                 flag -= 1
#             elif flag > 0 and d[idx] + d[idx - 1] == comd:
#                 maxd[idx] += maxd[idx - 1]
#                 flag -= 1
#         idx += 1
#     # print(d)
#     # print(maxd)

#     print("Case #{}: {}".format(x, max(maxd)), flush=True)

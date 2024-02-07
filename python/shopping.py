# import heapq


# def helper(reward):
#     nums = []
#     for i in reward:
#         heapq.heappush(nums, -i)
#     # print(nums)
#     ans = -heapq.heappop(nums)
#     # print(ans, nums)
#     i = 1
#     while nums:
#         temp = -heapq.heappop(nums)
#         print(temp, nums, i)
#         if temp - i <= 0:
#             break
#         ans += temp - i
#         print(ans)
#         i += 1
#     return ans

import heapq


# print(helper([5, 2, 2, 3, 1]))
def max_reward(reward: [int]):
    nums = []
    for i in reward:
        heapq.heappush(nums, -i)

    ans = -heapq.heappop(nums)
    i = 1
    while nums:
        curr = -heapq.heappop(nums)
        if curr - i <= 0:
            break
        ans += curr - i
        i += 1

    return ans


print(max_reward([5, 3, 2, 2, 1]))

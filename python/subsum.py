from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, curr = 0, 0
        numMap = defaultdict(int)
        numMap[0] = 1
        for i in range(len(nums)):
            curr += nums[i]
            if curr - k in numMap:
                count += numMap[curr - k]
            numMap[curr] += 1
        return count

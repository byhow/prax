# 41. First Missing Positive


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        n = len(nums) 
        while c < n:
            try:
                while (nums[c] > 0 and nums[c] <= n and nums[nums[c] - 1] != nums[c]):
                    nums[nums[c] - 1], nums[c] = nums[c], nums[nums[c] - 1]
            except:
                pass
            c += 1

        c = 0
        while (c < n and nums[c] == (c + 1)):
            c += 1
            
        return c + 1
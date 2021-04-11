class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def f(nums):
            if len(nums) < 3:
                return 1
            l = [i for i in nums if i < nums[0]]
            r = [i for i in nums if i > nums[0]]
            return comb(len(l) + len(r), len(r)) * f(l) * f(r)

        return (f(nums) - 1) % (10 ** 9 + 7)

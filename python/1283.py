class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        comp = lambda x: sum([ceil(n / x) for n in nums])

        l, r = 1, max(nums)
        while l <= r:
            mid = (l + r) // 2
            cur = comp(mid)
            if cur > threshold:
                l = mid + 1
            else:
                r = mid - 1

        return l

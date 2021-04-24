class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sums = [0]
        for i in nums:
            sums.append(sums[-1] + i)

        def sort(l, r):
            mid = (l + r) // 2
            if mid == l:
                return 0
            c = sort(l, mid) + sort(mid, r)
            i = j = mid
            for left in sums[l:mid]:
                while i < r and sums[i] - left < lower:
                    i += 1
                while j < r and sums[j] - left <= upper:
                    j += 1
                c += j - i
            sums[l:r] = sorted(sums[l:r])
            return c

        return sort(0, len(sums))
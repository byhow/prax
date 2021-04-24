class Solution:
    def reversePairs(self, nums):
        def mergeSort(start, end):
            if start >= end:
                return 0
            mid = (start + end) // 2
            cnt, j = mergeSort(start, mid) + mergeSort(mid + 1, end), mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - (mid + 1)
            nums[start : end + 1] = sorted(nums[start : end + 1])
            return cnt

        return mergeSort(0, len(nums) - 1)

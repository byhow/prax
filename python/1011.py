# 1011. Capacity To Ship Packages Within D Days
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            cur, mid, d = 0, (l + r) // 2, 1
            for i in weights:
                if cur + i > mid:
                    d += 1
                    cur = 0
                cur += i
            if d > D:
                l = mid + 1
            else:
                r = mid
        return l

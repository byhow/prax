class Solution:
    def createSortedArray(self, arr):
        m = max(arr)
        cnt = [0] * (m + 1)

        def update(x):
            while x <= m:
                cnt[x] += 1
                x += x & -x

        def get(x):
            res = 0
            while x > 0:
                res += cnt[x]
                x -= x & -x
            return res

        res = 0
        for i, a in enumerate(arr):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10 ** 9 + 7)
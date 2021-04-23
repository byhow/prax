class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(e):
            mid = len(e) // 2
            if mid:
                l, r = sort(e[:mid]), sort(e[mid:])
                for i in range(len(e))[::-1]:
                    if not r or l and l[-1][1] > r[-1][1]:
                        arr[l[-1][0]] += len(r)
                        e[i] = l.pop()
                    else:
                        e[i] = r.pop()
            return e

        arr = [0] * len(nums)
        sort(list(enumerate(nums)))
        return arr
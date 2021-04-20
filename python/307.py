class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = self.right = None


class NumArray:
    def __init__(self, nums):
        def create(nums, l, r):
            if l > r:
                return
            if l == r:
                root = Node(l, r)
                root.total = nums[l]
                return root
            mid = (l + r) // 2
            root = Node(l, r)
            root.left = create(nums, l, mid)
            root.right = create(nums, mid + 1, r)
            root.total = root.left.total + root.right.total
            return root

        self.root = create(nums, 0, len(nums) - 1)

    def update(self, i, val):
        def put(root, i, val):
            if root.start == root.end:
                root.total = val
                return val
            mid = (root.start + root.end) // 2
            if i <= mid:
                put(root.left, i, val)
            else:
                put(root.right, i, val)

            root.total = root.left.total + root.right.total
            return root.total

        return put(self.root, i, val)

    def sumRange(self, i, j):
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            mid = (root.start + root.end) // 2
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, i, j)

class Solution:
    def __init__(self):
        self.res = 0
        self.cache = {0: 1}

    def dfs(self, root, target, cur):
        if not root:
            return
        cur += root.val
        oldSum = cur - target
        self.res += self.cache.get(oldSum, 0)
        self.cache[cur] = self.cache.get(cur, 0) + 1

        self.dfs(root.left, target, cur)
        self.dfs(root.right, target, cur)
        self.cache[cur] -= 1

    def pathSum(self, root, target):
        self.dfs(root, target, 0)
        return self.res
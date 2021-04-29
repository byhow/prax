class Solution:
    def pathSum(self, root, rangeSum):
        res = []
        self.dfs(root, rangeSum, [], res)
        return res

    def dfs(self, root, rangeSum, leaves, res):
        if root:
            if not root.left and not root.right and rangeSum == root.val:
                leaves.append(root.val)
                res.append(leaves)
            self.dfs(root.left, rangeSum - root.val, leaves + [root.val], res)
            self.dfs(root.right, rangeSum - root.val, leaves + [root.val], res)

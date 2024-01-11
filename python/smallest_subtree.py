# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = {None: -1}

        def dfs(node, parent):
            if not node:
                return
            depth[node] = depth[parent] + 1
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        maxd = max(depth.values())

        def ans(node):
            if not node or depth[node] == maxd:
                return node
            l, r = ans(node.left), ans(node.right)
            return node if l and r else l or r

        return ans(root)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        cache = {}
        for i, v in enumerate(inorder):
            cache[v] = i

        def search(left, right):
            if left > right:
                return None
            v = TreeNode(postorder.pop())
            ind = cache[v.val]
            v.right = search(ind + 1, right)
            v.left = search(left, ind - 1)
            return v

        return search(0, len(inorder) - 1)
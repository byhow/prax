# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        vals = [(len(s[1]), s[2]) for s in re.findall("((-*)(\d+))", S)][::-1]

        def f(level):
            if not vals or vals[-1][0] != level:
                return None
            root = TreeNode(vals.pop()[1])
            root.left = f(level + 1)
            root.right = f(level + 1)
            return root

        return f(0)

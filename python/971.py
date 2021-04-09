# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.i = 0
        self.ret = []
        
        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.ret = [-1]
                    return
                self.i+=1
                if self.i < len(voyage) and node.left and node.left.val != voyage[self.i]:
                    self.ret.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)
            
        dfs(root)
        if self.ret and self.ret[0] == -1:
            self.ret = [-1]
        return self.ret
        

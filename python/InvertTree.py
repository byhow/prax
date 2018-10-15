class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


class Solution(object):
    def invertTree(self,root):
        if root:
          root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


root = TreeNode(5)
insert(root, TreeNode(1))
insert(root, TreeNode(4))
insert(root, TreeNode(7))
insert(root, TreeNode(8))
insert(root, TreeNode(2))
insert(root, TreeNode(3))
# inorder(root)
s = Solution()
s.invertTree(root)
inorder(root)

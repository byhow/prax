class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        leftd, rightd = self.getD(root.left), self.getD(root.right)
        if leftd == rightd:
            return 2 ** leftd + self.countNodes(root.right)
        else:
            return 2 ** rightd + self.countNodes(root.left)

    def getD(self, root):
        if not root:
            return 0
        return 1 + self.getD(root.left)
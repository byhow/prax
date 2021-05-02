class Solution:
    def longestUnivaluePath(self, root):
        self.longest = 0

        def transverse(root):
            if not root:
                return 0
            left_n, right_n = transverse(root.left), transverse(root.right)
            left = (left_n + 1) if root.left and root.left.val == root.val else 0
            right = (right_n + 1) if root.right and root.right.val == root.val else 0
            self.longest = max(self.longest, left + right)
            return max(left, right)

        transverse(root)
        return self.longest
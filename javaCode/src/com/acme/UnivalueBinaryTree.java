package com.acme;

import java.util.LinkedList;
import java.util.Queue;

public class UnivalueBinaryTree {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }


    public boolean isUnivalTree(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int v = root.val;
        while (!q.isEmpty()) {
            TreeNode t = q.poll();
            if(t.val!=v) return false;
            if(t.left!=null) {
                q.offer(t.left);
            }
            if (t.right!=null) {
                q.offer(t.right);
            }
        }

        return true;
    }


    // recursive DFS
//    public boolean isUnivalTree(TreeNode root) {
//        return helper(root, root.val);
//    }
//    public boolean helper(TreeNode t, int v) {
//        if (t == null) return true;
//        if (t.val != v) return false;
//        return helper(t.left, v) && helper(t.right, v);
//    }



}

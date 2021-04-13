/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
 var inorderTraversal = function(root) {
    let arr = []
    let cur = root
    let pre = null
    while (cur != null) {
        if (cur.left == null) {
            arr.push(cur.val)
            cur = cur.right
        } else {
            pre = cur.left
            while (pre.right != null) {
                pre = pre.right
            }
            pre.right = cur
            let temp = cur
            cur = cur.left
            temp.left = null
        }
    }
    return arr
    
};
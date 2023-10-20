/**
 * Definition for a binary tree node.
 */
/*
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function minDepth(root: TreeNode | null): number {
  if (!root) return 0;
  let stack = [root];
  let level = 1;

  while (stack.length > 0) {
    const newStack = [];
    while (stack.length > 0) {
      const node = stack.pop()!;
      if (!(node.left || node.right)) return level;
      if (node.left) newStack.push(node.left);
      if (node.right) newStack.push(node.right);
    }
    stack = newStack;
    level++;
  }
  return level;
}

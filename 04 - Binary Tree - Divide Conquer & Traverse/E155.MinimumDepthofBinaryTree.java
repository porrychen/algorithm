/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param root: The root of binary tree
     * @return: An integer
     */
    public int minDepth(TreeNode root) {
        // write your code here
        if (root == null) return 0;

        // method 1
        // if (root.left == null || root.right == null) {
        //     return Math.max(minDepth(root.left), minDepth(root.right)) + 1;
        // }

        // return Math.min(minDepth(root.left), minDepth(root.right)) + 1;

        // method 2
        return min(root);
    }

    private int min(TreeNode root) {
        if (root == null) return Integer.MAX_VALUE;

        if (root.left == null && root.right == null) return 1;

        return Math.min(min(root.left), min(root.right)) + 1;
    }
}

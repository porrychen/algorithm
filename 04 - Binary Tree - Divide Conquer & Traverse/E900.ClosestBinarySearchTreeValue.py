"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        upper, lower = root, root

        while root:
            if target > root.val:
                root, lower = root.right, root
            elif target < root.val:
                upper, root = root, root.left
            else:
                return root.val

        if abs(upper.val - target) <= abs(lower.val - target):
            return upper.val

        return lower.val

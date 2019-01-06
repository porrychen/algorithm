"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        self.traverse(root, result)

        return result

    def traverse(self, root, result):
        if root is None:
            return

        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root and (root.left or root.right):
            templeft = root.left
            tempright = root.right
            root.left = tempright
            root.right = templeft
            self.invertTree(tempright)
            self.invertTree(templeft)
        return root

        
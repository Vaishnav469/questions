# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        count = 1
        if not root.left and not root.right:
            return count
        
        countleft = 0
        if root.left:
            countleft += self.maxDepth(root.left)
        countright = 0
        if root.right:
            countright += self.maxDepth(root.right)
        
        countmax = max(countleft, countright)

        return count + countmax
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def maxDepth(root):
            nonlocal res
            if not root:
                return 0
            
            countleft = maxDepth(root.left)
            countright = maxDepth(root.right)
            
            diameter = countleft + countright
            res = max(res, diameter)
            return 1 + max(countleft, countright)
            
        maxDepth(root)
        return res
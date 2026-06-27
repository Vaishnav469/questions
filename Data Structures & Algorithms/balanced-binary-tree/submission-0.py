# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def maxDepth(root):
            nonlocal res
            if not root:
                return 0
            
            countleft = maxDepth(root.left)
            countright = maxDepth(root.right)
            
            difference = abs(countleft - countright)
            res = res and (difference <= 1)

            return 1 + max(countleft, countright)
            
        maxDepth(root)
        return res
            


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, ll, ul):
            if not root:
                return True
            if not (ll < root.val < ul):
                return False

            return valid(root.left, ll, root.val) and valid(root.right, root.val, ul)
        return valid(root, float("-inf"), float("+inf"))
      

        
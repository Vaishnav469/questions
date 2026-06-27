# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def traversal(root):
            if not root: return 1
            traversal(root.left)
            res.append(root.val)
            traversal(root.right)
        traversal(root)
        return res[k-1]        
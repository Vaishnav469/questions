# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root

        cur = root
        while cur:
            if cur.val == p.val or cur.val == q.val:
                res = cur
                break
            elif (cur.val > p.val and cur.val > q.val):
                cur = cur.left
            elif (cur.val < p.val and cur.val < q.val):
                cur = cur.right
            else:
                res = cur
                break
        return res

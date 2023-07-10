# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        counts=0
        if root == None:
            return 0
        l=Solution.minDepth(Solution,root.left)
        r=Solution.minDepth(Solution,root.right)
        if root.left == None and root.right==None:
            counts = min(r,l)+1
        elif root.left == None: 
            counts = max(r,l)+1
        elif root.right == None:
            counts = max(r,l)+1
        else:
            counts = min(r,l)+1   
        return counts

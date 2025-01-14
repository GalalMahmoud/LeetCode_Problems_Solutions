from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        max_in_row={}
        res=[]
        def dp(row:int,nroot=root):
            if nroot == None: return -2**32
            if row not in max_in_row: max_in_row[row]=[]
            max_in_row[row].append(nroot.val)
            dp(row+1, nroot.left)
            dp(row+1, nroot.right)
            return nroot
        dp(0,root)
        for k in max_in_row.keys():
            res.append(max(max_in_row[k]))
        return res
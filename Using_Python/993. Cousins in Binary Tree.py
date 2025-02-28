from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        stack = [(root, 1, root.val)]
        res = []

        while len(stack)>0:
            node, lvl, parent = stack.pop()
            if node:
                if node.val == x or node.val == y: res.append((node.val, lvl, parent))
                if node.left: stack.append((node.left, lvl+1, node.val))
                if node.right: stack.append((node.right, lvl+1, node.val))
        return res[0][1] == res[1][1] and res[0][2] != res[1][2]
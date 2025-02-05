from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(op_n, cls_n):
            if op_n==cls_n==n: 
                res.append("".join(stack))
                return
            if op_n < n:
                stack.append("(")
                backtrack(op_n+1,cls_n)
                stack.pop()
            if op_n > cls_n:
                stack.append(")")
                backtrack(op_n,cls_n+1)
                stack.pop()
            return res
        return backtrack(0,0)
    

# أفضل حل (ليس حلي)
# Best solution (Not mine)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res  = []
        def dfs(openP, closedP, s):
            if openP == closedP and openP + closedP == n*2:
                res.append(s)
                return
            if openP < n:
                dfs(openP+1, closedP, s+"(")
            if closedP < openP:
                dfs(openP, closedP+1, s+")")
        dfs(0, 0, "")
        return res
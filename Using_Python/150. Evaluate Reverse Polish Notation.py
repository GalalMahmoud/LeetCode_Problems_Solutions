from typing import List

# My solution
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = tokens[0]
        for t in tokens:
            if t.lstrip('-').isdigit(): stack.append(t)
            else:
                match t:
                    case '+': 
                        res = int(stack[-1])+int(stack[-2])
                    case '-':
                        res = int(stack[-2])-int(stack[-1])
                    case '*':
                        res = int(stack[-1])*int(stack[-2])
                    case '/':
                        if int(stack[-1]) != 0:
                            res = int(stack[-2])/int(stack[-1])
                        else: res = 0
                stack = stack[:-2]
                stack.append(res)
        return int(res)
    
###############################################

# Best solution for the problem on leetcode (not mine)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operator = {
            '+': lambda x, y: y + x,
            '-': lambda x, y: y - x,
            '*': lambda x, y: y * x,
            '/': lambda x, y: int(y/x)
        }
        for x in tokens:
            if x not in operator:
                stack.append(int(x))
            else:
                stack.append(operator[x](stack.pop(), stack.pop()))
                
        return int(stack[0])
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i,v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                stackIdx , _ = stack.pop()
                res[stackIdx]+= i - stackIdx
            stack.append((i,v))
        return res



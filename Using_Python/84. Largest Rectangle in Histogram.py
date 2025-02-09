from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0,heights[0])]
        res = heights[0]
        for i in range(1,len(heights)):
            statring = i
            while stack and heights[i] < stack[-1][1]:
                head = stack.pop()
                res = max(res,(i - head[0]) * head[1])
                statring = head[0]
            stack.append((statring,heights[i]))

        for i, h in stack:
            c = h*(len(heights)-i)
            res = max(res, c)
        return res
    


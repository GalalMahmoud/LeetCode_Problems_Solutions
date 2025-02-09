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
    

# أسرع حل (ليس حلي)
# Fastest solution (not mine)
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        L = []
        stackL = []
        for i in range(len(heights)):
            if(len(stackL) == 0):
                L.append(i)
                stackL.append(i)
                continue
                
            if(heights[stackL[-1]] < heights[i]):
                L.append(i)
            else:
                while len(stackL) > 0 and heights[stackL[-1]] >= heights[i]:
                    stackL.pop()
                if(len(stackL)):
                    L.append(stackL[-1]+1)
                else:
                    L.append(0)
            stackL.append(i)
        print(L)
        R = []
        stackR = []
        for i in range(len(heights)-1, -1, -1):
            if(len(stackR) == 0):
                R.append(i)
                stackR.append(i)
                continue
                
            if(heights[stackR[-1]] < heights[i]):
                R.append(i)
            else:
                while len(stackR) > 0 and heights[stackR[-1]] >= heights[i]:
                    stackR.pop()
                if(len(stackR) == 0):
                    R.append(len(heights)-1)
                else:
                    R.append(stackR[-1]-1)

            stackR.append(i)
        R.reverse()
        print(R)
        ans = 0
        for i in range(len(heights)):
            ans = max(ans, heights[i] * (R[i]-L[i]+1))
            
        return ans
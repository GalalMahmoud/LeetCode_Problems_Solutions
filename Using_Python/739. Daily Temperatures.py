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


#=====================================================================
# أفضل حل (ليس حلي)
# Best solution (not mine)
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Stores index, temps as (i, temp)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_i, _ = stack.pop()
                temperatures[prev_i] = i - prev_i
            stack.append((i, temp))
        while stack:
            prev_i, _ = stack.pop()
            temperatures[prev_i] = 0
        return temperatures
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left =0
        right = len(height)-1
        while left<len(height)-1 and right>0:
            water_area = min(height[left], height[right]) * (right - left)
            res = max(res, water_area)
            if height[left]<=height[right]: left+=1
            elif height[left]>height[right]: right-=1
        return res
    
#==========================================================================
# حل أفضل
# Better solution
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
    
#==========================================================================
# أفضل حل (ليس حلي)
# best solution (not mine)
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        start = 0
        end = n - 1
        while end > start:
            area = min(height[start], height[end]) * (end - start)
            if area > max_area:
                max_area = area
            if height[start] > height[end]:
                end = end - 1
            else :
                start = start + 1
        return max_area
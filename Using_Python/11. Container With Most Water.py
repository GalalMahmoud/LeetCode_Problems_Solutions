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
    

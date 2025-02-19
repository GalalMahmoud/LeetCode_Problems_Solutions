from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r= len(nums)-1
        res = nums[0]
        while l<=r:
            res = min(res, nums[l], nums[r])
            l+=1
            r-=1
        return res
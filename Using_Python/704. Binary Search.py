from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        med = len(nums)//2
        l = 0
        r = len(nums)
        while l<=r:
            med = (l+r)//2
            if nums[med] == target: return med
            elif nums[med] > target: r = med-1
            elif nums[med] < target: l = med+1
        return -1
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0]>=target: return 0
        i=1
        while i < len(nums)-1:
            # if nums[i-1]<target<nums[i+1] and nums[i]==target: return i
            if nums[i]>=target: return i
            elif nums[i-1]<target<nums[i+1] and nums[i]<target: return i+1
            # elif  nums[i-1]<target<nums[i+1] and nums[i]>target: return i-1
            i+=1
        if nums[-1]>=target: return len(nums)-1
        if nums[-1]<=target: return len(nums)



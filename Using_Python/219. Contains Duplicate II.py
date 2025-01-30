from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dt:dict = {}
        for i in range(len(nums)):
            if nums[i] not in dt: 
                dt[nums[i]]=[i]
                continue
            if abs(i-dt[nums[i]][-1]) <= k: return True
            dt[nums[i]].append(i)
        return False
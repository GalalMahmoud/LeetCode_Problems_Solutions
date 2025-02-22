from collections import defaultdict
from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n=len(nums)
        t=defaultdict(int)
        max_repeat = [nums[0],1]
        for i in range(n-1):
            if nums[i]==key:
                t[nums[i+1]]+=1
                if max_repeat[1]<=t[nums[i+1]]:
                    max_repeat = [nums[i+1],t[nums[i+1]]]
        return max_repeat[0]
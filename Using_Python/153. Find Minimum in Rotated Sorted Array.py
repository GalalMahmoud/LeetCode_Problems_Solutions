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
    

#============================================
# حل آخر بالبحث الثنائي
# Another solution with Binary Search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r= len(nums)-1
        while l<r:
            mid= l+(r-l)//2
            if nums[mid] >= nums[r]:
                l=mid+1
            else:
                r=mid-1
        return nums[l]
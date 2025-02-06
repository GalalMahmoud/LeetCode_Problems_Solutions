from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res =[]
        i = 0
        while  i<=len(nums)-1:
            # if not i<=len(nums)-1:
            #     break
            if nums[i] not in res:
                res.append(nums[i])
            else:
                del nums[i]
                continue
            i+=1
        return nums

# حل آخر
# Another solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0 
        while i<=len(nums)-2:
            if nums[i] == nums[i+1]:
                del nums[i+1]
                continue
            i+=1
        return len(nums)

# حل آخر
# Another solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0 
        lns = 0
        while i<=len(nums)-1:         
            if nums[i] == nums[lns]:
                i+=1
                continue
            lns+=1
            nums[i], nums[lns] = nums[lns], nums[i]
            i+=1
        return lns+1
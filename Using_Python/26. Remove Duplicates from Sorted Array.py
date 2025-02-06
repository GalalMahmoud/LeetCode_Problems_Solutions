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

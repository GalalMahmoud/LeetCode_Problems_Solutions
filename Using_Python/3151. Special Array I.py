from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        even_odd_flag = False if nums[0]%2 != 0 else True # false odd True Even
        for n in nums[1:]:
            if n%2 != 0 and not even_odd_flag: return False
            elif n%2 == 0 and even_odd_flag: return False
            even_odd_flag = not even_odd_flag
        return True
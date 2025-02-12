from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        forward=0
        backward=len(numbers)-1
        while True:
            if numbers[forward] + numbers[backward] < target: forward += 1
            elif numbers[forward] + numbers[backward] > target: backward -= 1
            elif forward == backward: return res
            else: 
                res.append(forward+1)
                res.append(backward+1)
                break
        return res
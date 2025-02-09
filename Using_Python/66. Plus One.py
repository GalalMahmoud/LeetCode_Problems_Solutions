from typing import List



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        com = int(self.combin(digits)) + 1
        return self.decombin(com)
    def combin(self, digits: List[int]) -> str:
        res=""
        for d in digits:
            res+=f"{d}"
        return res
    def decombin(self, digits: str) -> List[int]:
        res = []
        for d in str(digits):
            res.append(int(d))
        return res
    
######################################################
# حل آخر (ليس حلي)
# Another solution (not mine)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits 
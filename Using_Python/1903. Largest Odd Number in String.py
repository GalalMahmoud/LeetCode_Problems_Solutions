class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ''
        for i in range(len(num)):
            if int(num[-i-1]) % 2 != 0: 
                res = num[:len(num)-i]
                break
        return res
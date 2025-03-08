class Solution:
    def largestOddNumber(self, num: str) -> str:
        res = ''
        for i in range(len(num)):
            if int(num[-i-1]) % 2 != 0: 
                res = num[:len(num)-i]
                break
        return res
# ==============================================
# حل آخر
# Another solution
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0: return num[:i + 1]
        return ""
# ==============================================
# حل آخر
# Another solution
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if ord(num[i]) % 2 != 0: return num[:i + 1]
        return ""


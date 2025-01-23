import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]+', '', s).lower()
        if len(s)<2: return True
        for i in range(len(s)//2):
            if s[i]!=s[-i-1]: return False
        return True


# حل آخر
# Another solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

# أسرع حل
# Fastest solution on Leetcode
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(filter(str.isalnum, s.lower()))
        return string == string[::-1]

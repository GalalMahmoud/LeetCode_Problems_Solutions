class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=0
        s = s.strip()
        while i<len(s):
            if s[-i-1]==" ": return len(s[-i:])
            i+=1
        return len(s)
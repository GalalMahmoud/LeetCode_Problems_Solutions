class Solution:
    def clearDigits(self, s: str) -> str:
        i = 1
        while i < len(s):
            if s[i].isdigit() and not s[i-1].isdigit() or s[i-1].isdigit() and not s[i].isdigit():
                s=s[:i-1]+s[i+1:]
                if i>1:
                    i = i-1
            else:
                i+=1
        return s
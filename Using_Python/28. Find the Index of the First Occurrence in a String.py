class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i <=len(haystack)-len(needle):
            print(haystack[i:i+len(needle)])
            if haystack[i:i+len(needle)]==needle:
                return i
            i+=1
        return -1
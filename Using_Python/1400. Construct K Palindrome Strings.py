from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        if len(s) < k:
            return False
        count = Counter(s)
        solo=0
        for c,v in count.items():
            if v%2==1: solo+=1
        if k>=solo and k<=len(s):
            return True
        return False
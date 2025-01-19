# توجد حلول كثيرة سأذكر ثلاثة منها
# there are sevral ways to solve it


# أبطأ حل ولكن يعمل
# Slowest working solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        i=0
        while i<len(s):
            cidx = t.find(s[i])
            if cidx == -1:
                return False
            t= t[:cidx]+t[cidx+1:]
            i+=1
        return True
    
# ---------------------------------

# أداء سريع
# Faster solution
from typing import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        cs  = Counter(s)
        ct  = Counter(t)
        for c in s:
            if cs[c] != ct[c]:return False
        return True

# ---------------------------------

# ذاكرة ثابتة
# Fixed Memory
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        return sorted(s) == sorted(t)

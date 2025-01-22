from typing import List

# أسهل حل
# Easiest solution
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for st in strs:
            res +=st+'\n'
        return res

    def decode(self, s: str) -> List[str]:
        return s.split('\n')[:-1]

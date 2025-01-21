class Solution:
    roman_map = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    def romanToInt(self, s: str) -> int:
        res = 0
        cancel_next_flag = False
        for i in range(len(s)):
            # if s[i] is not s[-1] and self.roman_map[s[i]]<self.roman_map[s[i+1]]:
            if i < len(s)-1 and self.roman_map[s[i]]<self.roman_map[s[i+1]]:
                res += self.roman_map[s[i+1]] - self.roman_map[s[i]]
                cancel_next_flag = True
            elif cancel_next_flag:
                cancel_next_flag = False
                continue
            else:
                res += self.roman_map[s[i]]
        return res
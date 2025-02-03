class Solution:
    def isValid(self, s: str)->bool:
        stack=[]
        open_bracs ="{[("
        close_bracs ="}])"
        last_open = ""
        for i in range(len(s)):
            stack.append(s[i])
            if last_open=="" and s[i] in close_bracs:
                return False
            elif s[i] in open_bracs:
                last_open = s[i]
            elif s[i] in close_bracs:
                if open_bracs.index(last_open) != close_bracs.index(s[i]):
                    return False
                elif open_bracs.index(last_open) == close_bracs.index(s[i]):
                    stack.pop()
                    stack.pop()
                    if len(stack)>0: last_open = stack[-1]
                    else: last_open = ""
        return len(stack)==0

# حل آخر
# Another solution
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        opcls = {'[':']',
                '{':'}',
                '(':')'}
        for b in s:
            if b in opcls.keys(): stk.append(b)
            else: 
                if len(stk) == 0 or b != opcls[stk[-1]]:return False
                else: stk.pop()
        return True if len(stk)==0 else False
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        chars1 = [0]*26
        chars2 = [0]*26
        for i in range(len(s1)):
            chars1[ord('a') - ord(s1[i])] +=1
            chars2[ord('a') - ord(s2[i])] +=1
        
        for i in range(len(chars1)):
            if chars1[i]!=chars2[i]: return False

        non_dup_counter = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                non_dup_counter += 1
            if non_dup_counter > 2: return False
        return True
    

#===================================
# أفضل حل (ليس حلي)
# best solution (not mine)
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        if sorted(s1)!=sorted(s2):
            return False
        count=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
        if count!=2:
            return False
        return True
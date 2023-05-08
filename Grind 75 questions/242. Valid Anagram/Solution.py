class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        indecies = []
        if len(s) != len(t):
            return False
        for j in range(len(t)):
            for i in range(len(s)):
                if i == len(s):
                    return False
                if t[j] == s[i]:
                    s = s[:i]+s[i+1:]
                    break
        if len(s) == 0:
            return True
                

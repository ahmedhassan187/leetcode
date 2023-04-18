class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        iter = min(n,m)
        s = ""
        for i in range(iter):
            s += word1[i]+word2[i]
        if n>m:
            s += word1[iter:n]
        elif m>n:
            s += word2[iter:m]
        return s

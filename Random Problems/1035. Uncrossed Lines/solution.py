import numpy as np
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        res = np.zeros((m+1,n+1))
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1] == nums2[j-1]:
                    res[i,j] = res[i-1,j-1]+1
                else:
                    res[i,j] = max(res[i-1,j],res[i,j-1])
        return int(res[m,n])

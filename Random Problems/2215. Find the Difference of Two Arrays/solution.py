class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[],[]]
        for s in range(2):
            if s == 0:
                for i in range(len(nums1)):
                    flag = True
                    for j in range(len(nums2)):
                        if s == 0:
                            if nums1[i] == nums2[j]:
                                flag = False
                                break
                    if flag:
                        if not(nums1[i] in res[0]): 
                            res[0].append(nums1[i])
            if s ==1:
                for i in range(len(nums2)):
                    flag = True
                    for j in range(len(nums1)):
                        if nums2[i] == nums1[j]:
                            flag = False
                            break
                    if flag:
                        if not(nums2[i] in res[1]):
                            res[1].append(nums2[i])
        return res


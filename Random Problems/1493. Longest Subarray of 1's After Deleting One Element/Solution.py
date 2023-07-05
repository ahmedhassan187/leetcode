class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count=0
        maxones=0
        lcount = []
        for i in range(len(nums)):
            if nums[i] == 0:
                lcount.append(count)
                count = 0
            else:
                count =count+1
        lcount.append(count)
        if len(lcount) == 1:
            return lcount[0]-1
        print(lcount)
        for i in range(len(lcount)-1):
            summ = lcount[i]+lcount[i+1]
            if summ > maxones:
                maxones = summ
        return maxones

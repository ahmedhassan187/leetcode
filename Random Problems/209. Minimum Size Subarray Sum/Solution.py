class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if max(nums) >= target:
            return 1
        if sum(nums) < target:
            return 0
        elif sum(nums) == target:
            return n
        if len(nums) == 2:
            return 2
        i=0
        j=0
        summ = 0
        mn = math.inf
        while(j<n):
            summ += nums[j]
            while(summ >= target):
                summ -= nums[i]
                mn = min(j-i+1,mn)
                i=i+1
            j=j+1
        return mn

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left =0
        right=len(nums)
        while left<right:
            m = (right-left)//2
            if m<1:
                if target == nums[left]:
                    return left
                return -1
            if nums[left+m] == target:
                return left+m
            elif nums[left+m]>target:
                right -= m
            else:
                left += m
        return -1

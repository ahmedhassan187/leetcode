class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        items = []
        flag = True
        n = ((len(nums)-1)/3 + 1)
        print(n)
        n = int(n)
        for i in range(n):
            items.append([])
        for i in range(len(nums)):
            for j in range(n):
                if not items[j]:
                    items[j].append(nums[i])
                    items[j].append(1)
                    break
                elif nums[i] == items[j][0]:
                    items[j][1] = items[j][1] + 1
                    break
        print(items)
        for i in range(n):
            if items[i][1] != 3:
                return items[i][0]

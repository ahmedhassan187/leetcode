class Solution:
    def partitionString(self, s: str) -> int:
        temp = ""
        count = 1
        for i in s:
            if i in temp:
                count += 1
                temp = i
            else:
                temp = temp+i
        return count

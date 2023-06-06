class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        s = (arr[0]-arr[1]) 
        for i in range(len(arr)-1):
            if (arr[i]-arr[i+1]) != s:
                return False
        return True

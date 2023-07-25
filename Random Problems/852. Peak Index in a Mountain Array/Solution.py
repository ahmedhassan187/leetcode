class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = int(len(arr)/2)
        if len(arr)>2:
            if arr[n]>arr[n+1] and arr[n]>arr[n-1]:
                return n
            elif arr[n]>arr[n+1] and arr[n]<arr[n-1]:
                newarr = arr[:n]
                return self.peakIndexInMountainArray(newarr)
            elif  arr[n]<arr[n+1] and arr[n]>arr[n-1]:
                newarr = arr[n:]
                return n+self.peakIndexInMountainArray(newarr)
        else:
            return n

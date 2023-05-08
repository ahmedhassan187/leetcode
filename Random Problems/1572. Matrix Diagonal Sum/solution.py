class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        inv = len(mat[0])-1
        for i in range(len(mat[0])):
            ans += mat[i][i]
        for j in range(len(mat[0])):
            if j == (inv-j):
                continue
            ans += mat[j][inv-j]
        return ans

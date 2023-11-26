'''
- Link to Problem: https://leetcode.com/problems/largest-submatrix-with-rearrangements/
- Time Complexity: O(M * (N + Log N))
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        ans = 0

        for row in matrix:
            row.sort(reverse=True)
            for j in range(n):
                ans = max(ans, row[j] * (j + 1))
        
        return ans
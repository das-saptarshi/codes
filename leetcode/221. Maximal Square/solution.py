'''
- Link to Problem: https://leetcode.com/problems/maximal-square/
- Time Complexity: O(N * M)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] += min(
                        matrix[i-1][j], 
                        matrix[i][j-1], 
                        matrix[i-1][j-1]
                    )
                ans = max(ans, matrix[i][j])
        
        return ans ** 2
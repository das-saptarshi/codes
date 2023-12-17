'''
- Link to Problem: https://leetcode.com/problems/special-positions-in-a-binary-matrix/
- Time Complexity: O(R * C) [R = number of rows, C = number of columns]
- Space Complexity: O(R + C)
'''

from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        onesInRow = [0] * rows
        onesInCol = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    onesInRow[i] += 1
                    onesInCol[j] += 1
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and onesInRow[i] == 1 and onesInCol[j] == 1:
                    ans += 1
        
        return ans
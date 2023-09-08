'''
- Link to Problem: https://leetcode.com/problems/pascals-triangle/
- Time Complexity: O(NlogN)
- Space Complexity: O(NlogN)
'''

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        pascals = [[1]]

        for i in range(1, numRows):
            pascals.append([1])
            for j in range(1, len(pascals) - 1):
                pascals[-1].append(pascals[i-1][j-1] + pascals[i-1][j])
            pascals[-1].append(1)
        
        return pascals
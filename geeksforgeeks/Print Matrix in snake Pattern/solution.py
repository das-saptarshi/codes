'''
- Link to Problem: https://www.geeksforgeeks.org/problems/print-matrix-in-snake-pattern-1587115621/1
- Time Complexity: O(N^2)
- Space Complexity: O(N^2)
'''

from typing import List

class Solution:
    def snakePattern(self, matrix: List[List[int]]) -> List[int]: 
        ans = []
        
        for i in range(len(matrix)):
            if i % 2 == 0:
                ans.extend(matrix[i])
            else:
                ans.extend(matrix[i][::-1])
        return ans
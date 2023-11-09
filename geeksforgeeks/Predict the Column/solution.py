'''
- Link to Problem: https://www.geeksforgeeks.org/problems/predict-the-column/1
- Time Complexity: O(N*N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def columnWithMaxZeros(self, arr: List[List[int]], N: int) -> int:
        max_, index = 0, -1
        
        for j in range(N):
            total = 0
            for i in range(N):
                total += 1 - arr[i][j]
            
            if total > max_:
                index, max_ = j, total
        
        return index
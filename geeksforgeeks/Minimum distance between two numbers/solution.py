'''
- Link to Problem: https://www.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def minDist(self, arr: List[int], n: int, x: int, y: int) -> int:
        indexX = indexY = -1
        ans = float('inf')
        
        for i in range(n):
            if arr[i] == x:
                indexX = i
            if arr[i] == y:
                indexY = i
                
            if indexX != -1 and indexY != -1:
                ans = min(ans, abs(indexX - indexY))
        
        return -1 if ans == float('inf') else ans
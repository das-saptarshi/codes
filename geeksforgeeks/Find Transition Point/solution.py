'''
- Link to Problem: https://www.geeksforgeeks.org/problems/find-transition-point-1587115620/1
- Time Complexity: O(LogN)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def transitionPoint(self, arr: List[int], n: int) -> int: 
        start, end = 0, n - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if arr[mid] == 0:
                start = mid + 1
            else:
                end = mid - 1
        
        return start if start < n else -1
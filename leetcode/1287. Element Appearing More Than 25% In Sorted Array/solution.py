'''
- Link to Problem: https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        size = int(len(arr)*0.25) + 1
        
        for i in range(len(arr) - size):
            if arr[i] == arr[i+size]:
                return arr[i]
        return arr[-1]
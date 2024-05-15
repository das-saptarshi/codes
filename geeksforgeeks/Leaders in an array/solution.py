'''
- Link to Problem: https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def leaders(self, nums: List[int], n: int) -> List[int]:
        all_leaders = []
        
        for num in nums[::-1]:
            if not all_leaders or num >= all_leaders[-1]:
                all_leaders.append(num)
        
        return all_leaders[::-1]
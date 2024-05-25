'''
- Link to Problem: https://leetcode.com/problems/boats-to-save-people/
- Time Complexity: O(N * Log(N))
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boats += 1
        
        return boats
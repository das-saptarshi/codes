'''
- Link to Problem: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        seen = set()

        steps = 0

        for value in freq.values():
            steps += value
            while value > 0 and value in seen:
                value -= 1
            
            seen.add(value)
            steps -= value
        
        return steps
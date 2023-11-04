'''
- Link to Problem: https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left, default=0), n - min(right, default=n))
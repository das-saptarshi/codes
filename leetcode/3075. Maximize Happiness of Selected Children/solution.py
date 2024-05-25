'''
- Link to Problem: https://leetcode.com/problems/maximize-happiness-of-selected-children/
- Time Complexity: O(N * Log(N) + N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        return sum(max(0, happy - i) for i, happy in enumerate(happiness[:k]))
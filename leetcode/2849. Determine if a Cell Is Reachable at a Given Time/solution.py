'''
- Link to Problem: https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/
- Time Complexity: O(1)
- Space Complexity: O(1)
'''

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dist = max(abs(fy - sy), abs(fx - sx))
        if (sx, sy) == (fx, fy): return t != 1
        return dist <= t
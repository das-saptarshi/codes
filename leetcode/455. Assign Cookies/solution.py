'''
- Link to Problem: https://leetcode.com/problems/assign-cookies/
- Time Complexity: O(NlogN)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = ans = 0
        m, n = len(g), len(s)

        while i < m and j < n:
            if g[i] <= s[j]:
                ans += 1
                i += 1
            j += 1
        
        return ans
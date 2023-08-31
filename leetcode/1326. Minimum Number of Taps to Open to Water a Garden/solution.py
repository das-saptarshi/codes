# Link to Problem: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        maxReach = [0] * (n + 1)

        for i in range(n + 1):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])

            maxReach[start] = max(maxReach[start], end)
        
        currEnd = nextEnd = taps = 0

        for i in range(n + 1):
            if i > nextEnd:
                return -1
            if i > currEnd:
                taps += 1
                currEnd = nextEnd
            
            nextEnd = max(nextEnd, maxReach[i])
        
        return taps

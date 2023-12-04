'''
- Link to Problem: https://leetcode.com/problems/minimum-time-visiting-all-points/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def calculateTime(src, dst):
            x = abs(src[0] - dst[0])
            y = abs(src[1] - dst[1])

            return max(x, y)

        time = 0

        for i in range(1, len(points)):
            time += calculateTime(points[i - 1], points[i])
        
        return time
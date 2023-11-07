'''
- Link to Problem: https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

import math
from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        for i in range(n):
            dist[i] = math.ceil(dist[i] / speed[i])
            speed[i] = 0
        
        for d in dist:
            if d < n:
                speed[d] += 1
        
        for i in range(1, n):
            speed[i] += speed[i-1]
            if speed[i] > i:
                return i
        
        return n
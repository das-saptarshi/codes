'''
- Link to Problem: https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
- Time Complexity: O(G + G * A) [G: len of garbage, A: avg len of str in garbage]
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        
        travel = [0] + travel
        garbageFound = {
            'M': False,
            'G': False,
            'P': False
        }

        def update(x, i):
            totalTime = 1
            if not garbageFound[x]:
                garbageFound[x] = True
                totalTime += travel[i]
            return totalTime

        totalTime = 0
        for i in range(len(garbage) - 1, -1, -1):
            
            for x in garbage[i]:
                totalTime += update(x, i)
        
        return totalTime
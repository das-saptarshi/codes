'''
- Link to Problem: https://leetcode.com/problems/bus-routes/
- Time Complexity: O(N * M) [N: number of routes, M: avg stops in all the routes]
- Space Complexity: O(M_Max) [M_Max: max stop among all the routes]
'''

from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        maxStop = max(max(route) for route in routes)
        
        if maxStop < target: return -1
        minBusesToReach = [float('inf')] * (maxStop + 1)
        minBusesToReach[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                mini = min(minBusesToReach[stop] for stop in route) + 1
                for stop in route:
                    if minBusesToReach[stop] > mini:
                        minBusesToReach[stop] = mini
                        flag = True
        
        return minBusesToReach[target] if minBusesToReach[target] != float('inf') else -1
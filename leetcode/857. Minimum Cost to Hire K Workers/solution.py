'''
- Link to Problem: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
- Time Complexity: (N * (Log(N) + Log(K)))
- Space Complexity: O(N + K)
'''

import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        total_cost = float('inf')
        current_total_quality = 0
        highest_quality_workers = []
        wage_to_quality_ratio = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)])

        for i in range(n):
            heapq.heappush(highest_quality_workers, -wage_to_quality_ratio[i][1])
            current_total_quality += wage_to_quality_ratio[i][1]

            if len(highest_quality_workers) > k:
                current_total_quality += heapq.heappop(highest_quality_workers)

            if len(highest_quality_workers) == k:
                total_cost = min(
                    total_cost, 
                    current_total_quality * wage_to_quality_ratio[i][0]
                )
        
        return total_cost
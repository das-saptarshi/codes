'''
- Link to Problem: https://leetcode.com/problems/k-th-smallest-prime-fraction/
- Time Complexity: O(N * Log(N) + K * Log(N))
- Space Complexity: O(N)
'''

import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        priority_queue = []

        for i in range(len(arr)):
            heapq.heappush(priority_queue, (arr[i] / arr[-1], i, len(arr) - 1))
        

        for _ in range(k - 1):
            _, numerator_idx, denominator_idx = heapq.heappop(priority_queue)
            denominator_idx -= 1

            if denominator_idx > numerator_idx:
                heapq.heappush(
                    priority_queue, 
                    (
                        arr[numerator_idx] / arr[denominator_idx], 
                        numerator_idx, denominator_idx
                    )
                )
        

        _, numerator_idx, denominator_idx = heapq.heappop(priority_queue)

        return (arr[numerator_idx], arr[denominator_idx])
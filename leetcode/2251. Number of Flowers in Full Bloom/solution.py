'''
- Link to Problem: https://leetcode.com/problems/number-of-flowers-in-full-bloom/
- Time Complexity: O(NLogN)
- Space Complexity: O(N)
'''

import heapq
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowersHeap = []
        peopleHeap = []

        for start, end in flowers:
            heapq.heappush(flowersHeap, (start - 1, True))
            heapq.heappush(flowersHeap, (end, False))
        
        for person, time in enumerate(people):
            heapq.heappush(peopleHeap, (time, person))
        
        result = [0]*(len(people))
        bloomedFlowers = 0
        while peopleHeap:
            while flowersHeap and flowersHeap[0][0] < peopleHeap[0][0]:
                _, bloomed = heapq.heappop(flowersHeap)
                if bloomed:
                    bloomedFlowers += 1
                else:
                    bloomedFlowers -= 1
            
            _, person = heapq.heappop(peopleHeap)
            result[person] = bloomedFlowers
        
        return result
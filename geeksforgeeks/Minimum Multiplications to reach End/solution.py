'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import deque

class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        queue = deque([(start, 0)])
        
        seen = set()
        MOD = 100000
        
        while queue:
            num, steps = queue.popleft()
            if num == end:
                return steps
            
            for x in arr:
                nextNum = (num * x) % MOD
                if nextNum in seen:
                    continue
                seen.add(nextNum)
                queue.append((nextNum, steps+1))
        
        return -1
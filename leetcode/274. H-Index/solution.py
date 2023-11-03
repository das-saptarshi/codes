'''
- Link to Problem: https://leetcode.com/problems/h-index/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)

        for x in citations:
            if x >= n:
                buckets[-1] += 1
            else:
                buckets[x] += 1
        
        currCitations = 0
        for i in range(n, -1, -1):
            currCitations += buckets[i]
            if currCitations >= i:
                return i
        
        return 0
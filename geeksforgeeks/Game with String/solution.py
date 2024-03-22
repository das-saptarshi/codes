'''
- Link to Problem: https://www.geeksforgeeks.org/problems/game-with-string4100/1
- Time Complexity: O(N + KLog(P)) [N = number of characters in string s, K = value of k, P = number of unqiue values]
- Space Complexity: O(P)
'''

from collections import Counter
from heapq import heapify, heappush, heappop

class Solution:
    def minValue(self, s, k):
        counter = Counter(s)
        
        values = [-value for value in counter.values()]
        heapify(values)
        
        for _ in range(k):
            value = heappop(values) + 1
            if value == 0: continue
        
            heappush(values, value)
            
            
        return sum(value * value for value in values)
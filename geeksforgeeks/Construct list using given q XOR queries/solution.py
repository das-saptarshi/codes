'''
- Link to Problem: https://www.geeksforgeeks.org/problems/construct-list-using-given-q-xor-queries/1
- Time Complexity: O(N * Log(N))
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        ans = []
        xor = 0
        
        for query, value in reversed(queries):
            if query == 0: ans.append(value ^ xor)
            else: xor ^= value
        
        ans.append(xor)
        return sorted(ans)
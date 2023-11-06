'''
- Link to Problem: https://www.geeksforgeeks.org/problems/c-letters-collection4552/1
- Time Complexity: O(Q)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    ONE_HOP = ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1))
    TWO_HOP = ((-2,-2), (-2,-1), (-2,0), (-2,1), (-2,2), (-1,-2), (-1,2), (0,-2), (0,2), (1,-2), (1,2), (2,-2),
    (2,-1), (2,0), (2,1), (2,2))
    
    def matrixSum(self, n: int, m: int, mat: int, q: int, queries: List[List[int]]) -> List[int]:
        result = []
        for hop, r, c in queries:
            if hop == 1:
                hops = Solution.ONE_HOP
            else:
                hops = Solution.TWO_HOP
            
            ans = 0
            for i, j in hops:
                if (0 <= r + i < n and 0 <= c + j < m):
                    ans += mat[r+i][c+j]
            
            result.append(ans)
        return result
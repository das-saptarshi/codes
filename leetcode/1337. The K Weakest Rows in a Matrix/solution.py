'''
- Link to Problem: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
- Time Complexity: O(RLogR + N) [R = Number of Rows, N = Total Number of elements]
- Space Complexity: O(R)
'''

from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        def countSoldiers(row):
            
            try:
                return row.index(0)
            except:
                return len(row)
        
        soldiersCount = [countSoldiers(row) for row in mat]
        return sorted(list(range(len(mat))), key=lambda x : soldiersCount[x])[:k]
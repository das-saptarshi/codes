'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/boundary-traversal-of-matrix-1587115620/1
- Time Complexity: O(N + M)
- Space Complexity: O(N + M)
'''

from typing import List

class Solution:
    def BoundaryTraversal(self, matrix: List[List[int]], n: int, m: int) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        if n == 1 or m == 1:
            return [x for row in matrix for x in row]
            
        boundaryElements = []
        directions = [0, 1, 0, -1]
        dx, dy = 0, 1
        x, y = directions[dx], directions[dy]
        
        sizes = [n, m]
        iSize = 1
        
        r = c = 0
        
        for _ in range(4):
            size = sizes[iSize]
            iSize = (iSize + 1) % len(sizes)
            
            for _ in range(size - 1):
                try:
                    boundaryElements.append(matrix[r][c])
                except:
                    return []
                r += x
                c += y
            
            dx, dy = (dx + 1) % len(directions), (dy + 1) % len(directions)
            x, y = directions[dx], directions[dy]
        
        return boundaryElements
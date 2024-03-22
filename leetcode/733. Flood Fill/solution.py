'''
- Link to Problem: https://leetcode.com/problems/flood-fill/
- Time Complexity: O(R * C)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        
        rows, cols = len(image), len(image[0])
        baseColor = image[sr][sc]

        def fill(row, col):
            if not (0 <= row < rows and 0 <= col < cols and image[row][col] == baseColor):
                return

            image[row][col] = color

            for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                fill(row + r, col + c)
        
        fill(sr, sc)
        return image
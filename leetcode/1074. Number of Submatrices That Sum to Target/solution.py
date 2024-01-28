'''
- Link to Problem: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
- Time Complexity: O(R * C^2)
- Space Complexity: O(Target)
'''


from typing import List
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row, col = len(matrix), len(matrix[0])

        for r in range(row):
            for c in range(1, col):
                matrix[r][c] += matrix[r][c - 1]


        ans = 0

        for start in range(col):
            for end in range(start, col):
                subMatrixSum = 0
                freq = defaultdict(int)
                freq[0] = 1

                for r in range(row):
                    prefixSum = 0 if start == 0 else matrix[r][start - 1]
                    subMatrixSum += matrix[r][end] - prefixSum

                    ans += freq[subMatrixSum - target]
                    freq[subMatrixSum] += 1
        
        return ans
# Link to Problem: https://leetcode.com/problems/combinations/description/
# Time Complexity: O(comb(n, k) * k) [comb(n, k) - combination of n over k for picking k numbers for n numbers, and k for copying the combination array to the result]
# Space Complexity: O(comb(n, k))

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def solve(index_i, index_j, combination):
            if index_j == k:
                result.append(combination[:])
                return

            for i in range(index_i, n):
                combination[index_j] = i + 1
                solve(i + 1, index_j + 1, combination)
        
        solve(0, 0, [0]*k)
        return result
# Link to Problem: https://leetcode.com/problems/permutations/description/
# Time Complexity: O(n * n!) [Finding all the permutations is 'n!', and copying n elements to the final array is 'n']
# Space Complexity: O(n)

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []
        permutation = [0]*n
        seen = [False]*n

        def solve(index):
            if index == n:
                permutations.append(permutation[:])
                return
            
            for i in range(n):
                if seen[i]:
                    continue
                seen[i] = True
                permutation[index] = nums[i]
                solve(index + 1)
                seen[i] = False
        
        solve(0)
        return permutations
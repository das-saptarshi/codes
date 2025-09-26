'''
- Link to Problem: https://leetcode.com/problems/valid-triangle-number/
- Time Complexity: O(N ^ 2)
- Space Complexity: O(1)
'''

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        triangles = 0

        nums.sort()
        for i in range(n):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                
                triangles += k - j - 1
        
        return triangles
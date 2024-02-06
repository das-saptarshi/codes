'''
- Link to Problem: https://leetcode.com/problems/product-of-array-except-self/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        zeros = index = 0
        product = 1
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
                index = i
                continue
            product *= num
        
        if zeros > 1:
            return [0] * n
    
        if zeros == 1:
            return [0] * index + [product] + [0] * (n - index - 1)

        return [product // num for num in nums]
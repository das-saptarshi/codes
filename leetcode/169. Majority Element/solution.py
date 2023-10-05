'''
- Link to Problem: https://leetcode.com/problems/majority-element/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = nums[0]

        for num in nums:
            if num == element:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                count = 1
                element = num
        
        return element
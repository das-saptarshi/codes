'''
- Link to Problem: https://leetcode.com/problems/rearrange-array-elements-by-sign/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = 0, 1
        ans = [0] * len(nums)

        for num in nums:
            if num > 0:
                ans[positive] = num
                positive += 2
            else:
                ans[negative] = num
                negative += 2
        
        return ans
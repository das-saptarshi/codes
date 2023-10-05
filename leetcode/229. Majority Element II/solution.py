'''
- Link to Problem: https://leetcode.com/problems/majority-element-ii/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [x for x, value in Counter(nums).items() if value > len(nums) // 3]
        
'''
- Link to Problem: https://leetcode.com/problems/single-number-iii/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        return [num for num, freq in Counter(nums).items() if freq == 1]
'''
- Link to Problem: https://leetcode.com/problems/sort-colors/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List
from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = defaultdict(int)

        for num in nums: freq[num] += 1

        index = 0
        for num in range(3):
            for _ in range(freq[num]):
                nums[index] = num
                index += 1
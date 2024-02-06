'''
- Link to Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            x, y = numbers[left], numbers[right]

            if x + y == target:
                return [left + 1, right + 1]
            elif x + y < target:
                left += 1
            else:
                right -= 1
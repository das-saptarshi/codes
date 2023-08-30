# Link to Problem: https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1]
        ans = 0

        for x in nums[::-1]:
            if x > last:
                steps = (x - 1) // last
                last = x // (steps + 1)
                ans += steps
            else:
                last = x
        
        return ans
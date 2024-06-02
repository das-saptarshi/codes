'''
- Link to Problem: https://leetcode.com/problems/reverse-string/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1


        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

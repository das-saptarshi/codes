'''
- Link to Problem: https://leetcode.com/problems/integer-break/
- Time Complexity: O(1)
- Space Complexity: O(1)
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        if (n <= 3):
            return n - 1

        div, mod = divmod(n, 3)

        if mod == 0:
            return 3 ** div
        elif mod == 1:
            return 3 ** (div - 1) * 4
        else:
            return 3 ** div * 2
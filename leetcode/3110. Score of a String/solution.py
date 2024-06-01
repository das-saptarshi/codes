'''
- Link to Problem: https://leetcode.com/problems/score-of-a-string/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i - 1]) - ord(s[i])) for i in range(1, len(s)))
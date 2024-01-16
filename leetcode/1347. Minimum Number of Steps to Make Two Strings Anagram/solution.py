'''
- Link to Problem: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
- Time Complexity: O(S + T)
- Space Complexity: O(S + T)
'''

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = Counter(s)
        tCount = Counter(t)

        return sum(max(0, sCount[x] - tCount.get(x, 0)) for x in sCount.keys())
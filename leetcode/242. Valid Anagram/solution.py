'''
- Link to Problem: https://leetcode.com/problems/valid-anagram/
- Time Complexity: O(S + T)
- Space Complexity: O(S + T)
'''

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
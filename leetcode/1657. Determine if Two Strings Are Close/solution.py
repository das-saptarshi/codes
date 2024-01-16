'''
- Link to Problem: https://leetcode.com/problems/determine-if-two-strings-are-close/
- Time Complexity: O(NLogN)
- Space Complexity: O(N)
'''

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        if set(freq1.keys()) != set(freq2.keys()): return False

        return sorted(freq1.values()) == sorted(freq2.values())
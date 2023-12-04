'''
- Link to Problem: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
- Time Complexity: O(N * K) [N: number of words, K: avg len of a word]
- Space Complexity: O(K)
'''

from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCount = Counter(chars)
        ans = 0
        for word in words:
            wordCount = Counter(word)
            if all(value <= charCount[key] for key, value in wordCount.items()):
                ans += len(word)
        return ans
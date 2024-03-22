'''
- Link to Problem: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
- Time Complexity: O(N * K) [N = number of words, K = avg length of word]
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            if word == word[::-1]:
                return word
        
        return ''
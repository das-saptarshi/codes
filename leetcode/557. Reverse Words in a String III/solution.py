'''
- Link to Problem: https://leetcode.com/problems/reverse-words-in-a-string-iii/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())
'''
- Link to Problem: https://leetcode.com/problems/determine-if-string-halves-are-alike/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    VOWELS = set('aeiouAEIOU')
    def halvesAreAlike(self, s: str) -> bool:
        return self.vowels(s[:len(s) // 2]) == self.vowels(s[len(s) // 2:])
    
    def vowels(self, s: str) -> int:
        return len([x for x in s if x in self.VOWELS])
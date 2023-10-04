'''
- Link to Problem: https://leetcode.com/problems/roman-to-integer/
- Time Complexity: O(N) [N: length of S]
- Space Complexity: O(1)
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = numerals[s[0]]
        
        for i in range(1, len(s)):
            total += numerals[s[i]]
            if numerals[s[i]] > numerals[s[i-1]]:
                total -= 2*numerals[s[i-1]]
        return total
                
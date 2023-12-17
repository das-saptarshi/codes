'''
- Link to Problem: https://leetcode.com/problems/largest-odd-number-in-string/
- Time Complexity: O(N) [N = len of string num]
- Space Complexity: O(1)
'''

class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds = set('13579')
        for i in range(len(num) - 1, -1, -1):
            if num[i] in odds:
                return num[:i + 1]
        
        return ''
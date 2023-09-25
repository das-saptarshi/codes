'''
- Link to Problem: https://leetcode.com/problems/find-the-difference/
- Time Complexity: O(T) [T: len of str t]
- Space Complexity: O(1)
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = [0]*26
        base = ord('a')

        for i in range(len(s)):
            freq[ord(t[i]) - base] += 1
            freq[ord(s[i]) - base] -= 1
        freq[ord(t[-1]) - base] += 1
        
        for i in range(len(freq)):
            if freq[i] > 0:
                return chr(i + base)
'''
- Link to Problem: https://leetcode.com/problems/is-subsequence/
- Time Complexity: O(T) [T = len(t)]
- Space Complexity: O(1)
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        
        if n > len(t):
            return False

        index = 0

        for x in t:
            if x == s[index]:
                index += 1
            if index == n:
                return True
        
        return False
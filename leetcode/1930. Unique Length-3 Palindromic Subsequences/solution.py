'''
- Link to Problem: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique = {}

        for i in range(len(s)):
            if s[i] not in unique:
                unique[s[i]] = [i, i]
            else:
                unique[s[i]][1] = i
        
        ans = 0
        for key, (start, end) in unique.items():
            if start == end: continue
            ans += len(set(s[start + 1: end]))
        return ans
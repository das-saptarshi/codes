'''
- Link to Problem: https://leetcode.com/problems/count-number-of-homogenous-substrings/
- Time Complexity: O(S) [S: length of s]
- Space Complexity: O(1)
'''

class Solution:
    def countHomogenous(self, s: str) -> int:
        s = s + ' '
        result = 0
        MOD = 10**9 + 7
        continousLen = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                continousLen += 1
            else:
                result = ((continousLen + 1) * continousLen // 2 + result) % MOD
                continousLen = 1

        return result
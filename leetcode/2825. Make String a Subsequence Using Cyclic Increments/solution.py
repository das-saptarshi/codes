'''
- Link to Problem: https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/
- Time Complexity: O(1)
- Space Complexity: O(1)
'''

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        index, n = 0, len(str2)
        base = ord('a')

        for s in str1:
            x = (ord(s) - base + 1) % 26 + base

            if s == str2[index] or chr(x)  == str2[index]:
                index += 1
                if index == n:
                    return True

        return False 
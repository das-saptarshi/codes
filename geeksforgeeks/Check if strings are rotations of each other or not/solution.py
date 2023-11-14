'''
- Link to Problem: https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1
- Time Complexity: O(S1 + S2) [S1: len of s1, S2: len of s2]
- Space Complexity: O(1)
'''

class Solution:
    def areRotations(self, s1: str, s2: str) -> bool:
        return s1 in (s2 + s2)
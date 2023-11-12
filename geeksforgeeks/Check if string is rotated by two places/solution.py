'''
- Link to Problem: https://www.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def isRotated(self, str1: str, str2: str) -> bool:
        return (str1 == str2[-2:] + str2[:-2]) or (str1 == str2[2:] + str2[:2])
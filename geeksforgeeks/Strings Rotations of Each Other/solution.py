'''
- Link to Problem: https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1
- Time Complexity: O(1)
- Space Complexity: O(1)
'''

class Solution:
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        return s2 in (s1 +  s1)

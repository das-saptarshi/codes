'''
- Link to Problem: https://www.geeksforgeeks.org/problems/pangram-checking-1587115620/1
- Time Complexity: O(S) [S = length of string s]
- Space Complexity: O(1)
'''

class Solution:
    def checkPangram(self, s: str) -> bool:
        alphabets = set(s.lower())
        return all(x in alphabets for x in 'qwertyuiopasdfghjklzxcvbnm')
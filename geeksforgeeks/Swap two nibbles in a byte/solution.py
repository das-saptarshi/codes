'''
- Link to Problem: https://www.geeksforgeeks.org/problems/swap-two-nibbles-in-a-byte0446/1
- Time Complexity: O(1)
- Space Complexity: O(1)
'''

class Solution:
    def swapNibbles (self, n):
        return ((n & 15) << 4) | (n >> 4)
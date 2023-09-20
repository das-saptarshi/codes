'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/rotate-bits4524/1
- Time Complexity: O(1)
- Space Complexity: O(1)
'''

class Solution:
    def rotate(self, N, D):
        bits = bin(N)[2:].rjust(16, '0')
        D = D % 16
        return int(bits[D:] + bits[:D], 2), int(bits[-D:] + bits[:-D], 2)

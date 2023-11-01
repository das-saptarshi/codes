'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/form-a-number-divisible-by-3-using-array-digits0717/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def isPossible(self, N, arr):
        return int(sum(arr) % 3 == 0)
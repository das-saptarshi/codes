'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/perfect-numbers3207/1
- Time Complexity: O(sqrt(N))
- Space Complexity: O(1)
'''

class Solution:
    def isPerfectNumber(self, N):
        if N <= 1:
            return 0
            
        total = 1
        for i in range(2, int(N**(0.5)) + 1):
            if N % i == 0:
                total += i + (N // i)

        return int(total == N)
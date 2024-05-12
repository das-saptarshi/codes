'''
- Link to Problem: https://www.geeksforgeeks.org/problems/minimum-number-of-steps-to-reach-a-given-number5234/1
- Time Complexity: O(D)
- Space Complexity: O(1)
'''

class Solution:
    def minSteps(self, d):
        for n in range(1, 2 * d):
            if ((n * (n + 1) // 2) + d) % 2 == 0 and ((n * (n + 1) // 2)) >= d:
                return n
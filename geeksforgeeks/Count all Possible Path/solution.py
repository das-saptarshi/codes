'''
- Link to Problem: https://www.geeksforgeeks.org/problems/castle-run3644/1
- Time Complexity: O(N^2)
- Space Complexity: O(1)
'''

class Solution:
    def isPossible(self, paths):
        n = len(paths)

        for i in range(n):
            if sum(paths[i]) % 2 != 0:
                return 0

        return 1
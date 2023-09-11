'''
- Link to Problem: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    MOD = 10**9 + 7
    def countOrders(self, n: int) -> int:
        ans = 1
        for i in range(2, n + 1):
            ans = (ans * (2 * i - 1) * i) % self.MOD

        return ans
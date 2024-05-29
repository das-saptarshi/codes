'''
- Link to Problem: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)

        operations = carry = 0

        for i in range(n - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2 == 1:
                operations += 2
                carry = 1
            else:
                operations += 1
        
        return operations + carry
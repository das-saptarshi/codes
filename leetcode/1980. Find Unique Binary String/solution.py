'''
- Link to Problem: https://leetcode.com/problems/find-unique-binary-string/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''


from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(int(num, 2) for num in nums)
        n = len(nums)

        for num in range(n + 1):
            if num not in nums:
                return bin(num)[2:].rjust(n, '0')
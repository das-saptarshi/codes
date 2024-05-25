'''
- Link to Problem: https://leetcode.com/problems/palindrome-partitioning/
- Time Complexity: O(2 ^ N)
- Space Complexity: O(2 ^ N)
'''

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def generate(left, right, subset):
            if right == len(s):
                if left == right:
                    subsets.append(subset[:])
                return

            word = s[left: right + 1]

            if word == word[::-1]:
                generate(right + 1, right + 1, subset + [word])
            generate(left, right + 1, subset)
        
        subsets = []
        generate(0, 0, [])
        return subsets
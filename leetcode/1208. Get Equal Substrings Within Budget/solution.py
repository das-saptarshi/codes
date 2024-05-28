'''
- Link to Problem: https://leetcode.com/problems/get-equal-substrings-within-budget/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        start = max_len = cost = 0
        n = len(s)

        for i in range(n):
            cost += abs(ord(s[i]) - ord(t[i]))

            while cost > max_cost:
                cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            
            max_len = max(max_len, i - start + 1)
            
        return max_len
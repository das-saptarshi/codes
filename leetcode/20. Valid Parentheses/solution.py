'''
- Link to Problem: https://leetcode.com/problems/valid-parentheses/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for x in s:
            if x not in pairs:
                stack.append(x)
            elif stack and stack[-1] == pairs[x]:
                stack.pop()
            else:
                return False
        
        return not stack
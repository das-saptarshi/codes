'''
- Link to Problem: https://leetcode.com/problems/backspace-string-compare/
- Time Complexity: O(S + T)
- Space Complexity: O(Max(S, T))
'''

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.buildString(S) == self.buildString(T)

    def buildString(self, s: str) -> str:
        stack = []

        for x in s:
            if x == '#':
                if stack: stack.pop()
            else:
                stack.append(x)
        
        return ''.join(stack)
'''
- Link to Problem: https://leetcode.com/problems/remove-duplicate-letters/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIndex = {x: i for i, x in enumerate(s)}
        stack = []
        seen = set()

        for i in range(len(s)):
            x = s[i]
            if x in seen: continue
            while stack and ord(x) < ord(stack[-1]) and lastIndex[stack[-1]] > i:
                seen.remove(stack.pop())

            seen.add(x)
            stack.append(x)
        
        return ''.join(stack)
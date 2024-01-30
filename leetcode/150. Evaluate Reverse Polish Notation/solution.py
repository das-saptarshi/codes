'''
- Link to Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-+').isnumeric():
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == '+': stack.append(num1 + num2)
                elif token == '-': stack.append(num1 - num2)
                elif token == '*': stack.append(num1 * num2)
                elif token == '/': stack.append(int(num1 / num2))
            
        return stack.pop()
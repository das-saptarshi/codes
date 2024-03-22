'''
- Link to Problem: https://leetcode.com/problems/zigzag-conversion/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        code = ['' for _ in range(numRows)]

        index = 0
        for x in s:
            code[index] += x

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            
            index += step
        
        return ''.join(code)
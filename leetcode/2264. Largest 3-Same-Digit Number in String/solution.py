'''
- Link to Problem: https://leetcode.com/problems/largest-3-same-digit-number-in-string/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = -1
        prev = ''
        count = 0

        for x in num:
            if x == prev:
                count += 1
                if count == 3:
                    largest = max(largest, int(x))
            else:
                prev = x
                count = 1
        
        return '' if largest == -1 else str(largest) * 3
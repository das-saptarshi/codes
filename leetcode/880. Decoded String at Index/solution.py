'''
- Link to Problem: https://leetcode.com/problems/decoded-string-at-index/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:

        length = i = 0

        while length < k:
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i += 1

        for j in range(i-1, -1, -1):
            x = s[j]

            if x.isdigit():
                length //= int(x)
                k %= length
            else:
                if k == 0 or k == length:
                    return x
                length -= 1
                
'''
- Link to Problem: https://leetcode.com/problems/minimum-window-substring/
- Time Complexity: O(S + T)
- Space Complexity: O(1)
'''

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        totalChars = len(freq)
        m = len(s)
        left = right = charsCovered = 0
        ans = ''

        while right < m:
            x = s[right]

            if x in freq:
                freq[x] -= 1
                if freq[x] == 0:
                    charsCovered += 1
            
            if charsCovered == totalChars:

                while left <= right and charsCovered == totalChars:
                    y = s[left]
                    if y in freq:
                        freq[y] += 1
                        if freq[y] == 1:
                            charsCovered -= 1
                    left += 1
                if not ans or len(ans) > (right - left + 1):
                    ans = s[left - 1: right + 1]
            right += 1

        return ans
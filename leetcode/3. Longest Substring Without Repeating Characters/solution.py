'''
- Link to Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)

        start = ans = 0

        for end in range(len(s)):
            freq[s[end]] += 1

            while freq[s[end]] > 1:
                freq[s[start]] -= 1
                start += 1

            ans = max(ans, end - start + 1)
        
        return ans
'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/count-number-of-substrings4528/1
- Time Complexity: O(N)
- Space Complexity: O(K)
'''


from collections import defaultdict

class Solution:
    def substrCount (self,s, k):
        return self.atMostK(s, k) - self.atMostK(s, k-1)
    
    def atMostK(self, s, k):
        start = end = ans = 0
        freq = defaultdict(int)
        
        while end < len(s):
            freq[s[end]] += 1
            
            while len(freq) > k:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    freq.pop(s[start])
                start += 1
            end += 1
            ans += end - start + 1
        
        return ans
'''
- Link to Problem: https://www.geeksforgeeks.org/problems/find-number-of-times-a-string-occurs-as-a-subsequence3020/1
- Time Complexity: O(N * M)
- Space Complexity: O(M)
'''

class Solution:
    def countWays(self, s : str, t : str) -> int:
        MOD = 10 ** 9 + 7
        n, m = len(s), len(t)
        number_of_subsequences = [0] * (m + 1)
        
        for i in range(1, n + 1):
            prev = [1] + number_of_subsequences[1:]
            
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    number_of_subsequences[j] = (prev[j - 1] + prev[j]) % MOD
                else:
                    number_of_subsequences[j] = prev[j] % MOD
        
        return number_of_subsequences[m]
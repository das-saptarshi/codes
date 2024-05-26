'''
- Link to Problem: https://leetcode.com/problems/student-attendance-record-ii/
- Time Complexity: O(N)
- Space Complexity: O(6 * N)
'''

class Solution:
    def checkRecord(self, n: int) -> int:
        
        def eligible_combinations(n, total_absences, consecutive_lates):
            if total_absences >= 2 or consecutive_lates >= 3:
                return 0
            
            if n == 0:
                return 1
            
            if memo[n][total_absences][consecutive_lates] != -1:
                return memo[n][total_absences][consecutive_lates]
            
            count = (eligible_combinations(n - 1, total_absences, 0) + 
                    eligible_combinations(n - 1, total_absences + 1, 0) +
                    eligible_combinations(n - 1, total_absences, consecutive_lates + 1)) % MOD
                
            memo[n][total_absences][consecutive_lates] = count
            return count
        
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]
        MOD = 10 ** 9 + 7
        return eligible_combinations(n, 0, 0)
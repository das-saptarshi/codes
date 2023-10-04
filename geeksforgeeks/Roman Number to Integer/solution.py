'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/roman-number-to-integer3201/1
- Time Complexity: O(N) [N: length of S]
- Space Complexity: O(1)
'''

class Solution:
    def romanToDecimal(self, S): 
        literals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = literals[S[0]]
        
        for i in range(1, len(S)):
            total += literals[S[i]]
            if literals[S[i]] > literals[S[i - 1]]:
                total -= 2 * literals[S[i - 1]]
            
        return total
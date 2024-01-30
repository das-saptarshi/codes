'''
- Link to Problem: https://www.geeksforgeeks.org/problems/lcs-of-three-strings0028/1
- Time Complexity: O(N1 * N2 * N3)
- Space Complexity: O(N1 * N2 * N3)
'''

class Solution:
    def LCSof3(self, A:str, B:str, C:str, n1:int, n2:int, n3:int) -> int:
        lcs = [[[0] * (n3 + 1) for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                for k in range(1, n3 + 1):
                    
                    if A[i - 1] == B[j - 1] and B[j - 1] == C[k - 1]:
                        lcs[i][j][k] = lcs[i-1][j-1][k-1] + 1
                    
                    else:
                        lcs[i][j][k] = max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1])
    
        return lcs[n1][n2][n3]
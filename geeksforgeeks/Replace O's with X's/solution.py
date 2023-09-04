'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/replace-os-with-xs0052/1
- Time Complexity: O(n*m)
- Space Complexity: O(1)
'''


class Solution:
    def fill(self, n, m, mat):
        mappings = {'X': 'X', 'O': 'X', 'Y': 'O'}
        
        for i in range(m):
            self.flood(0, i, n, m, mat)
            self.flood(n-1, i, n, m, mat)
        
        for i in range(n):
            self.flood(i, 0, n, m, mat)
            self.flood(i, m-1, n, m, mat)
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = mappings[mat[i][j]]
                
        return mat

                

    def flood(self, r, c, n, m, mat):
        if not (0 <= r < n and 0 <= c < m and mat[r][c] == 'O'):
            return
        mat[r][c] = 'Y'
        self.flood(r + 1, c, n, m, mat)
        self.flood(r, c + 1, n, m, mat)
        self.flood(r - 1, c, n, m, mat)
        self.flood(r, c - 1, n, m, mat)
'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/boolean-matrix-problem-1587115620/1
- Time Complexity: O(R*C)
- Space Complexity: O(R+C)
'''

def booleanMatrix(matrix):
    r, c = len(matrix), len(matrix[0])
    
    rows, cols = set(), set()
    
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                rows.add(i)
                cols.add(j)
    
    
    for x in rows:
        for j in range(c):
            matrix[x][j] = 1
    
    
    for y in cols:
        for i in range(r):
            matrix[i][y] = 1
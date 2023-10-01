'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def findTwoElement(self, arr, n):
        a = b = -1
        total, currTotal = n * (n + 1) // 2, sum(arr)
        
        for i in range(n):
            x = abs(arr[i])
            
            if arr[x - 1] < 0:
                b = x
                break
            else:
                arr[x - 1] *= -1
        
        a = total - currTotal + b
        return [b, a]
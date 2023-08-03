# Link to Problem: https://practice.geeksforgeeks.org/problems/reverse-a-stack/1
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List
from sys import setrecursionlimit

setrecursionlimit(10000)

class Solution:
    def reverse(self, stack, queue=[]): 
        if not stack:
            return 
        
        queue.append(stack.pop())
        self.reverse(stack, queue)
        stack.append(queue.pop(0))



# Driver Code
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# Driver Code Ends
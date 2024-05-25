'''
- Link to Problem: https://www.geeksforgeeks.org/problems/you-and-your-books/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def max_Books(self, n: int, k: int, heights: List[int]) -> int:
        
        max_books = 0
        current_books = 0
        
        for height in heights:
            
            if height <= k:
                current_books += height
            else:
                max_books = max(max_books, current_books)
                current_books = 0
        
        return max(max_books, current_books)
'''
- Link to Problem: https://www.geeksforgeeks.org/problems/pythagorean-triplet3018/1
- Time Complexity: O(N^2)
- Space Complexity: O(N)
'''


from typing import List

class Solution:
    def checkTriplet(self,arr: List[int], n: int):
        squares = set(x**2 for x in arr)
        for square1 in squares:
            for square2 in squares:
                if (square1 + square2) in squares:
                    return True

        return False
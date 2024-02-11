'''
- Problem Statement: Given an array and an operation -> foo(index, value), the value can be either 1 or -1, if foo(index, value) is called, it will add value to all elements from index till end of the array, find minimum number of operation to make all array elements 0.
- Time Complexity: O(N)
- Space Complexity: O(1)

Note: Not sure if the solution will return minimum number of operations or not.
'''

from typing import List

class Solution:

    def minOperationsToMakeElementsZero(self, nums: List[int]):
        change = 0
        operations = 0

        for num in nums:
            num += change

            if num == 0: continue

            operations += abs(num)
            change -= num

        return operations
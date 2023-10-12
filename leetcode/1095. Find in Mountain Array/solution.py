'''
- Link to Problem: https://leetcode.com/problems/find-in-mountain-array/
- Time Complexity: O(LogN)
- Space Complexity: O(1)
'''

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def get(self, index: int) -> int: pass
   def length(self) -> int: pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.findPeak(mountain_arr)
        ans = self.binarySearch(mountain_arr, 0, peak, target)
        if ans >= 0: return ans
        return self.binarySearchReverse(mountain_arr, peak, mountain_arr.length()- 1, target)
    
    def findPeak(self, arr: 'MountainArray'):
        start, end = 0, arr.length() - 1

        while start < end:
            mid = (start + end) // 2

            if arr.get(mid) < arr.get(mid + 1):
                start = mid + 1
            else:
                end = mid
        
        return start
    
    def binarySearch(self, arr: 'MountainArray', start, end, target):
        while start <= end:
            mid = (start + end) // 2
            x = arr.get(mid)
            if x == target:
                return mid
            elif target > x:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    
    def binarySearchReverse(self, arr: 'MountainArray', start, end, target):
        while start <= end:
            mid = (start + end) // 2
            x = arr.get(mid)
            if x == target:
                return mid
            elif target > x:
                end = mid - 1
            else:
                start = mid + 1
        return -1
        
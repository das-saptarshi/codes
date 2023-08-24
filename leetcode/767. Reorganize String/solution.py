# Link to Problem: https://leetcode.com/problems/reorganize-string/
# Time Complexity: O(nlogn) (Actual is O(n + 2nlogn), where n is for heapification and 2nlogn is for pop and push of items n times from the heap).
# Space Complexity: O(n) (for Heap)


from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = [(-value, key) for key, value in freq.items()]
        heapq.heapify(heap)

        ans = '*'

        while heap:
            count, x = heapq.heappop(heap)
            count *= -1

            if ans[-1] != x:
                ans += x
                self.addToHeap(heap, count - 1, x)
            elif heap:
                newCount, newX = heapq.heappop(heap)
                newCount *= -1
                ans += newX
                self.addToHeap(heap, count, x)
                self.addToHeap(heap, newCount - 1, newX)
            else:
                return ''
        
        return ans[1:]
    
    def addToHeap(self, heap, count, x):
        if count == 0:
            return
        
        heapq.heappush(heap, (-count, x))
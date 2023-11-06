'''
- Link to Problem: https://leetcode.com/problems/seat-reservation-manager/
- Time Complexity: O(LogN)
- Space Complexity: O(N)
'''

import heapq

class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.seats = 0

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        self.seats += 1
        return self.seats

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.seats:
            self.seats -= 1
        else:
            heapq.heappush(self.heap, seatNumber)
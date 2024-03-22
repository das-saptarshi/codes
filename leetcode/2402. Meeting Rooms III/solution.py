'''
- Link to Problem: https://leetcode.com/problems/meeting-rooms-iii/
- Time Complexity: O(MLogM + MLogR) [M = number of meetings, R = number of rooms]
- Space Complexity: O(R)
'''

from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        usedFreq = [0] * n
        rooms = list(range(n))
        heapify(rooms)
        endTimes = []

        for startsAt, endsAt in meetings:
            while endTimes:
                availableAt, room = endTimes[0]

                if availableAt <= startsAt:
                    heappop(endTimes)
                    heappush(rooms, room)
                else:
                    break

            if not rooms:
                availableAt, room = heappop(endTimes)
                usedFreq[room] += 1
                heappush(endTimes, (availableAt + (endsAt - startsAt), room))
            else:
                room = heappop(rooms)
                usedFreq[room] += 1
                heappush(endTimes, (endsAt, room))
        
        
        return usedFreq.index(max(usedFreq))
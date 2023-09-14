'''
- Link to Problem: https://leetcode.com/problems/reconstruct-itinerary/
- Time Complexity: O(TlogT + T) [T: number of tickets]
- Space Complexity: O(T)
'''

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        numberOfTickets = len(tickets)

        airports = defaultdict(list)
        for fromAirport, toAirport in tickets:
            airports[fromAirport].append([toAirport, False])
        
        for value in airports.values():
            value.sort()

        def solve(airport, ticketsUsed):
            if ticketsUsed == numberOfTickets:
                return [airport]
            
            for i in range(len(airports[airport])):
                nextAirport, visited = airports[airport][i]
                if not visited:
                    airports[airport][i][1] = True
                    ans = solve(nextAirport, ticketsUsed + 1)
                    if ans:
                        return [airport] + ans
                    airports[airport][i][1] = False
            
            return []
        
        return solve('JFK', 0)
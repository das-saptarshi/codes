'''
- Link to Problem: https://www.geeksforgeeks.org/problems/account-merge/1
- Time Complexity: O(S + T + T * Log(T)) [S = (N + M), T = (S * M) N = number of accounts, M = avg number of emails in each account]
- Space Complexity: O(S + T)
- Metadata:
    - Algorithm: Disjoint Set
'''

from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        disjoint_set = DisjointSet(n)
        
        email_index = {}
        
        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_index:
                    disjoint_set.union(index, email_index[email])
                else: 
                    email_index[email] = index
        
        email_group = defaultdict(list)
        
        for email, index in email_index.items():
            leader = disjoint_set.find(index)
            email_group[leader].append(email)
        
        result = []
        
        for index, emails in email_group.items():
            name = accounts[index][0]
            result.append([name] + sorted(emails))
        
        return result
        
        
    
    
class DisjointSet:
    def __init__(self, size: int) -> None: 
        self.size = size
        self.parent = [i for i in range(size + 1)]
        self.rank = [1] * (size + 1)
        
    
    def find(self, node: int) -> int:
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    
    def union(self, node_1: int, node_2: int) -> None:
        parent_1 = self.find(node_1)
        parent_2 = self.find(node_2)
        
        if parent_1 == parent_2: return
    
        if self.rank[parent_1] >= self.rank[parent_2]:
            self.parent[parent_2] = parent_1
            self.rank[parent_1] += self.rank[parent_2]
        else:
            self.parent[parent_1] = parent_2
            self.rank[parent_2] += self.rank[parent_1]
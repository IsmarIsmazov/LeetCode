from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        curr = self.root[x]
        while curr != self.root[curr]:
            self.root[curr] = self.find(self.root[curr])
            curr = self.root[curr]
        return curr
    
    def merge(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return True
        
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_x] > self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.rank[root_x] += 1

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        union = UnionFind(n)

        # Merge components that share the same edge
        for u, v, w in edges:
            union.merge(u, v)

        # Key: Root of connected component
        # Value: Bitwise AND of all edges in connected component
        connected_component_min_cost = defaultdict(int)

        # Compute bitwise AND for all edges of the same connected component
        for u, v, w in edges:
            if union.find(u) == union.find(v):
                root = union.find(u)
                if root not in connected_component_min_cost:
                    connected_component_min_cost[root] = w
                else:
                    connected_component_min_cost[root] &= w

        min_cost = []
        for origin, destination in query:
            # In case nodes are in different connected components
            if union.find(origin) != union.find(destination):
                min_cost.append(-1)
            else:
                min_cost.append(connected_component_min_cost[union.find(origin)])
        return min_cost
    

    obj = Solution()
    print(obj.minimumCost(4, [[1,2,3],[3,4,4]], [[1,4],[2,3],[3,1]]))
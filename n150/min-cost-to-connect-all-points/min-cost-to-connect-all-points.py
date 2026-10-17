# https://leetcode.com/problems/min-cost-to-connect-all-points

'''
Key Insights:
    - I didn't do this like a strict interview style practice problem,
      mostly because I coulnd't remember how to do MST off the top of my
      head
    - It was kind of a fun blast-from-the-past going through my OMSCS
      CS6515 hw7 notes on MST
    - Basically referenced my old notes on how to do MST with Kruskal's
      algo + UnionFind data structure
    - We'll see if I can actually regurtitate this info in a real
      interview
'''

from itertools import combinations
from dataclasses import dataclass

@dataclass
class Edge:
    weight: int
    a: int
    b: int

class UnionFind:
    def __init__(self, n_points):
        self.parents = list(range(n_points))
        self.rankings = [0] * n_points

    def find(self, p):
        assert p < len(self.parents), "find() got point index out of range"
        if self.parents[p] != p:
            # path compression
            self.parents[p] = self.find(self.parents[p])
        return self.parents[p]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            # Root already shared, this would create a cycle
            return False

        # ranked union - insert the smaller tree under the bigger tree
        if self.rankings[root_a] < self.rankings[root_b]:
            root_a, root_b = root_b, root_a
        self.parents[root_b] = root_a

        # update rankings if needed
        if self.rankings[root_a] == self.rankings[root_b]:
            self.rankings[root_a] += 1
        return True

class Solution(object):
    def manhattan(self, a, b):
        # print(f"manhattan. a={a}, b={b}")
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # create a list of all the edges between points
        # with their weights
        n = len(points)
        edges = list(combinations(list(range(n)), 2))
        weights = []
        for edge in edges:
            a, b = edge
            weight = self.manhattan(points[a], points[b])
            weights.append(Edge(weight, a, b))
        weights.sort(key=lambda x: x.weight)
        edges = weights

        # kruskal's alg + union-find
        uf = UnionFind(n)
        # For the problem itself, we only need the total and not the
        # mst. I'm tracking it just for fun.
        mst = []
        total = 0
        for edge in weights:
            if uf.find(edge.a) != uf.find(edge.b):
                mst.append(edge)
                total += edge.weight
                assert uf.union(edge.a, edge.b), "attempt to create cycle"
        return total

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
        ([[3,12],[-2,5],[-4,1]], 18),
    ]
    for (points, solution) in tests:
        result = sol.minCostConnectPoints(points)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


# https://leetcode.com/problems/max-area-of-island

from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()
        self.mx = 0
        for i, row in enumerate(self.grid):
            for j, _ in enumerate(row):
                self.mx = max(self.dfs(i, j), self.mx)
                # self.mx = max(self.bfs(i, j), self.mx)
        return self.mx

    # Recursive + DFS
    def dfs(self, x, y):
        if (
            x < 0
            or y < 0
            or x >= self.rows
            or y >= self.cols
            or (x,y) in self.visited
            or self.grid[x][y] != 1
        ):
            return 0
        self.visited.add((x,y))
        area = 1 + self.dfs(x-1, y) \
            + self.dfs(x+1, y) \
            + self.dfs(x, y+1) \
            + self.dfs(x, y-1)
        return area
    
    # Iterative + BFS
    def bfs(self, x, y):
        q = deque([(x, y)])
        area = 0
        while len(q) > 0:
            x, y = q.pop()
            if (
                x < 0
                or y < 0
                or x >= self.rows
                or y >= self.cols
                or (x,y) in self.visited
                or self.grid[x][y] != 1
            ):
                continue
            self.visited.add((x,y))
            area += 1
            q.append((x+1, y))
            q.append((x-1, y))
            q.append((x, y+1))
            q.append((x, y-1))
        return area

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                [0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]
            ],
            6,
        )
    ]
    for (grid, solution) in tests:
        result = sol.maxAreaOfIsland(grid)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid

class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        mx = 0
        for i in range(self.rows):
            for j in range(self.cols):
                mx = max(mx, self.step(i, j, set()))
        return mx

    def step(self, i, j, path):
        if (i < 0
            or i >= self.rows
            or j < 0
            or j >= self.cols
            or self.grid[i][j] == 0
            or (i, j) in path
        ):
            return 0
        path.add((i,j))
        mx = sum([
            self.step(i+1, j, path),
            self.step(i, j+1, path),
            self.step(i-1, j, path),
            self.step(i, j-1, path),
        ])
        return mx + self.grid[i][j]
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]], 7),
        ([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]], 1),
        ([[4,5,5], [0,10,0]], 24),
        ([[8,6], [2,6]], 22)
    ]
    for (grid, solution) in tests:
        result = sol.findMaxFish(grid)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


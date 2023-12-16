# https://leetcode.com/problems/special-positions-in-a-binary-matrix

# First solution.
from itertools import repeat
class Solution(object):

    def only_one(self, grid, itr):
        count = 0
        for i, j in itr:
            if grid[i][j] == 1:
                count += 1
                if count > 1:
                    break
        return count == 1

    def numSpecial(self, grid):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        cache = {'rows': set(), 'cols': set()}
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == 1
                    and i not in cache['rows']
                    and j not in cache['cols']
                    and self.only_one(grid, zip(repeat(i), range(0, cols)))
                    and self.only_one(grid, zip(range(0, rows), repeat(j)))
                ):
                    count += 1
                    cache['rows'].add(i)
                    cache['cols'].add(j)
        return count

# Second solution. Based off common solution from other people's
# submissions. Make 2 passes: first pass sum the row/col counts. Second
# pass for every cell equal to 1, check if the row/col counts are also
# 1, and if so count that as a solution.
class Solution(object):
    def numSpecial(self, grid):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols
        out = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == 1
                    and row_count[i] == 1
                    and col_count[j] == 1
                ):
                    out += 1
        return out

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,0,0],[0,0,1],[1,0,0]], 1),
        ([[1,0,0],[0,1,0],[0,0,1]], 3),
    ]
    for (mat, solution) in tests:
        result = sol.numSpecial(mat)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


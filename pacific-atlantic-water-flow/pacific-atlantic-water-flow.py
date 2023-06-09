# https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        self.heights = heights
        self.rows = len(self.heights)
        self.cols = len(self.heights[0])
        solutions = []

        for (i, row) in enumerate(self.heights):
            for (j, _cell) in enumerate(row):
                ret = self.step(dict(), set(), pow(10, 5)+1, i, j)
                print(f"heights[{i},{j}] = {heights[i][j]}, ret = {ret}")
                if ret == 3:
                    solutions.append([i, j])
        return solutions

    def step(self, memo, seen, last, i, j):
        if (i,j) in memo:
            return memo[(i,j)]
        if i < 0 or j < 0:
            return 1
        if i >= self.rows or j >= self.cols:
            return 2
        if (i,j) in seen:
            return 0
        if self.heights[i][j] > last:
            return 0

        seen.add((i,j))
        a = self.step(memo, seen, self.heights[i][j], i + 1, j)
        b = self.step(memo, seen, self.heights[i][j], i - 1, j)
        c = self.step(memo, seen, self.heights[i][j], i, j + 1)
        d = self.step(memo, seen, self.heights[i][j], i, j - 1)
        seen.remove((i,j))
       
        ret = a | b | c | d
        if (i,j) in memo:
            memo[(i,j)] = memo[(i,j)] | ret
        else:
            memo[(i,j)] = ret
        return ret

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]],
            [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]],
        ),
        (
            [[10,10,10],[10,1,10],[10,10,10]],
            [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]],
        )
    ]
    for (heights, solution) in tests:
        result = sol.pacificAtlantic(heights)
        solution, result = sorted(solution), sorted(result)
        # print(f"result {result} != solution {solution}")
        assert solution == result, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


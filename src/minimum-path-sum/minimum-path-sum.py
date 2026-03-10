# https://leetcode.com/problems/minimum-path-sum

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m] * n
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if i > 0 and j > 0:
                    dp[i][j] = val + min(dp[i-1][j], dp[i][j-1])
                elif i > 0:
                    dp[i][j] = val + dp[i-1][j]
                elif j > 0:
                    dp[i][j] = val + dp[i][j-1]
                else:
                    dp[i][j] = val
        return dp[n-1][m-1]
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1,3,1],[1,5,1],[4,2,1]],
            7,
        ),
        (
            [[1,2,3],[4,5,6]],
            12,
        ),

    ]
    for (grid, solution) in tests:
        result = sol.minPathSum(grid)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")



# https://leetcode.com/problems/find-missing-and-repeated-values

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        seen = [0 for _ in range(pow(n, 2))]
        for row in grid:
            for num in row:
                seen[num-1] += 1
        out = [-1, -1]
        for (i, count) in enumerate(seen):
            if count == 0:
                out[1] = i + 1
            elif count == 2:
                out[0] = i + 1
        assert out[0] != -1 and out[1] != -1, \
            "fail to find both outputs"
        return out
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,3],[2,2]], [2,4]),
        ([[9,1,7],[8,9,2],[3,4,6]], [9,5]),
    ]
    for (grid, solution) in tests:
        result = sol.findMissingAndRepeatedValues(grid)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


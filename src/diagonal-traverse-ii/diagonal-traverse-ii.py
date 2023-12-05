# https://leetcode.com/problems/diagonal-traverse-ii

class Solution(object):
    def findDiagonalOrder(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        x = len(grid)
        y = len(grid[0]) # note: assume rectangular 2d array
        diags = x+y-1
        mid = diags // 2
        solution = []
        for l in range(diags):
            # print("********")
            if l <= mid: 
                itr = zip(reversed(range(l+1)), range(l+1))
            else:
                itr = zip(reversed(range(l-mid, mid+1)), range(l-mid, mid+1))
            for i, j in itr:
                # print(f"i={i}, j={j}")
                if i < x and j < len(grid[i]):
                    solution.append(grid[i][j])
        return solution


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                [1,2,3],
                [4,5,6],
                [7,8,9],
            ],
            [1,4,2,7,5,3,8,6,9]
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10,11,12],
                [13,14,15,16],
            ],
            [1,5,2,9,6,3,13,10,7,4,14,11,8,15,12,16]
        ),
        (
            [
                [1,2,3],
                [4],
                [5,6,7],
                [8],
                [9,10,11]
            ],
              [1,4,2,5,3,8,6,9,7,10,11]
            # [1,4,2,5,3,8,6,7]
        )
        (
            [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]],
            [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
        )
    ]
    for (grid, solution) in tests:
        # print("********************")
        result = sol.findDiagonalOrder(grid)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


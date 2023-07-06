# https://leetcode.com/problems/set-matrix-zeroes

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        x = len(matrix)
        y = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(x):
            for j in range(y):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            for j in range(y):
                matrix[row][j] = 0
        for col in cols:
            for i in range(x):
                matrix[i][col] = 0
        return matrix
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1,1,1],[1,0,1],[1,1,1]],
             [[1,0,1],[0,0,0],[1,0,1]],
        ),
        (
            [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
            [[0,0,0,0],[0,4,5,0],[0,3,1,0]],
        )
    ]
    for (matrix, solution) in tests:
        result = sol.setZeroes(matrix)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


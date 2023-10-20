# https://leetcode.com/problems/pascals-triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]
        if numRows == 1:
            return triangle
        for i in range(1, numRows):
            row = list()
            for j in range(i + 1):
                a = triangle[i-1][j-1] if j-1 >= 0 else 0
                b = triangle[i-1][j] if j < len(triangle[i-1]) else 0
                row.append(a+b)
            triangle.append(row)
        return triangle

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            5,
            [
                [1],
                [1,1],
                [1,2,1],
                [1,3,3,1],
                [1,4,6,4,1],
            ],
        ),
        (
            1,
            [[1]],
        ),
    ]
    for (numRows, solution) in tests:
        result = sol.generate(numRows)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


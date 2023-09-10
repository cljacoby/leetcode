# https://leetcode.com/problems/search-a-2d-matrix

import numpy as np

'''
- Using numpy for ease of slicing 2d matrices (i.e. I'm lazy)
- I still suck at writing a simple binary algorithm. I normally mess
  some combination of:
    - The exit condition
    - The index determination
    - Calculation of the midpoint
- Really need to just practice this problem type and build the muscle
  memory
'''

class Solution(object):
    def searchMatrix(self, matrix, x):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        matrix = np.array(matrix)
        (i, _) = self.bisect(matrix[:, 0], 0, len(matrix), x)
        row = matrix[i]
        (j1, j2) = self.bisect(row, 0, len(row), x)
        if row[j1] == x \
        or (len(row) > j2 and row[j2] == x):
            return True
        return False

    def bisect(self, nums, i, j, x):
        if j - i <= 1:
            return (i, j)
        m = (j + i) // 2
        if nums[i] <= x < nums[m]:
            return self.bisect(nums, i, m, x)
        else:
            return self.bisect(nums, m, j, x)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            3,
            True,
        ),
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            13,
            False,
        ),
        (
            [[1, 1]],
            0,
            False,
        ),
        (
            [[1], [3]],
            3,
            True,
        ),
    ]
    for (t, (matrix, x, solution)) in enumerate(tests):
        result = sol.searchMatrix(matrix, x)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

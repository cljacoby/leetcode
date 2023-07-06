# https://leetcode.com/problems/spiral-matrix

class _Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        x = 0
        y = 0
        y_start = 0
        x_start = 0
        x_end = rows
        y_end = cols
        direct = 'right'
        out = []
        while len(out) < rows * cols:
            if direct == "right":
                for y in range(y, y_end):
                    out.append(matrix[x][y])
                y_end -= 1
                x_start += 1
                direct = "down"
            if direct == "down":
                for x in range(x, x_end):
                    out.append(matrix[x][y])
                x_end -= 1
                y_end -= 1
                direct = "left"
            if direct == "left":
                for y in range(y, y_start, -1):
                    out.append(matrix[x][y])
                y_start += 1
                x_end -= 1
                direct = "up"
            if direct == "up":
                for x in range(x, x_start, -1):
                    out.append(matrix[x][y])
                x_start += 1
                y_start += 1
                direct = "right"
            else:
                raise ValueError("invalid direct")
        return out

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.max_x = self.rows - 1
        self.max_y = self.cols - 1
        self.min_x = 0
        self.min_y = 0
        self.out = []
        self.step("right", 0, 0)

    def step(self, direct, x, y):
        if len(self.out) == self.rows * self.cols:
            retur
        self.out.append(self.matrix[x][y])
        if (x,y) == (self.min_x, self.max_y):
            self.min_x += 1
            self.step("down", x + 1, y)
        if (x,y) == (self.max_x, self.max_y):
            self.max_y -= 1
            self.step("left", x, y - 1)
        if (x,y) == (self.max_x, self.min_y):
            self.max_x -= 1
            self.step("up", x + 1, y)
        if (x,y) == (self.min_x, self.min_y):
            self.min_y += 1
            self.step("right", x, y + 1)
        else:
            if direct == "right":
                self.step(direct, x, y + 1)
            elif direct == "down":
                self.step(direct, x + 1, y)
            elif direct == "right":
                self.step(direct, x, y - 1)
            elif direct == "up":
                self.step(direct, x - 1, y)
            else:
                ValueError("Bad Direction")

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ],
            [1,2,3,6,9,8,7,4,5],
        ),
        (
            [
                [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]
            ],
            [1,2,3,4,8,12,11,10,9,5,6,7],
        ),
    ]
    for (matrix, solution) in tests:
        result = sol.spiralOrder(matrix)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


# https://leetcode.com/problems/spiral-matrix

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.size = self.m * self.n
        self.seen = dict()
        self.out = list()
        self.step(0, 0, 0)
        return self.out

    def new_direction(self, old):
        '''
        0 - right
        1 - down
        2 - left
        3 - up
        '''
        if old == 3:
            return 0
        return old + 1

    def next(self, i, j, d):
        if d == 0:
            return (i, j+1)
        if d == 1:
            return (i+1, j)
        if d == 2:
            return (i, j-1)
        if d == 3:
            return (i-1, j)

    def step(self, i, j, d):
        if len(self.out) == self.size:
            return
        self.out.append(self.matrix[i][j])
        self.seen[(i,j)] = True
        (x, y) = self.next(i, j, d)
        if (
            x < 0
            or y < 0
            or x >= self.m
            or y >= self.n
            or (x,y) in self.seen
        ):
            d = self.new_direction(d)
            (x, y) = self.next(i, j, d)
        self.step(x, y, d)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1,2,3],[4,5,6],[7,8,9]],
            [1,2,3,6,9,8,7,4,5],
        ),
        (
            [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
            [1,2,3,4,8,12,11,10,9,5,6,7],
        ),
    ]
    for (matrix, solution) in tests:
        result = sol.spiralOrder(matrix)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


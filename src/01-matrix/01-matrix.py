# https://leetcode.com/problems/01-matrix

import json
from collections import deque

'''
Key Insights:
    - My main obstacle was thinking of the problem as starting at the
      non-zero cells, and recursing (DFS) until I reached a zero cell, and 
      then adding up the stack frames on the way up to get the path
    - Key was to use BFS and start at the zero cells, and count out to
      the non-zero cells
'''

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q = deque()
        rows = len(mat)
        cols = len(mat[0])
        d = [ (-1, 0), (1, 0), (0, -1), (0, 1), ]
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = "*"
        while len(q) > 0:
            (x,y) = q.popleft()
            for (up, down) in d:
                i, j = x+up, y+down
                if (i < 0
                    or j < 0
                    or i >= rows
                    or j >= cols
                    or mat[i][j] != '*'
                ):
                    continue
                mat[i][j] = mat[x][y] + 1
                q.append((i,j))
        return mat


if __name__ == "__main__":
    sol = Solution()
    t1 = json.load(open("test1.json"))
    tests = [
        (
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        ),
        (
            [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
            [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        ),
        (
            t1['matrix'],
            t1['solution']
        )
    ]
    for (matrix, solution) in tests:
        result = sol.updateMatrix(matrix)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

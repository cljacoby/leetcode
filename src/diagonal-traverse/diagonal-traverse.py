# https://leetcode.com/problems/diagonal-traverse

"""
3 x 3:
0,0; 0,1; 1,1; 2,1; 1,1; 0,2; 1,3; 2,1; 2,2;

when we step out of grid:
    if dr == up+right:
        - try moving column rigtward
        - elif try moving column downward
        - else done
    elif dr == down+left:
        - try moving row downward
        - else try moving column rightward


3 x 2:
"""


class Solution(object):
    def findDiagonalOrder(self, mat):
        n = len(mat)
        m = len(mat[0])
        i = 0
        j = 0
        end = (n - 1, m - 1)
        # 0: up+right, 1: down+left
        dr = 0
        arr = []
        while True:
            arr.append(mat[i][j])
            if dr == 0:
                right = j + 1 < m
                up = i - 1 >= 0
                down = i + 1 < n
                if right and up:
                    j += 1
                    i -= 1
                    continue
                dr = 1
                if right:
                    j += 1
                elif down:
                    i += 1
                elif (i, j) == end:
                    break
                else:
                    assert False, "bad up-right move"
            else:
                left = j - 1 >= 0
                down = i + 1 < n
                right = j + 1 < m
                if left and down:
                    j -= 1
                    i += 1
                    continue
                dr = 0
                if down:
                    i += 1
                elif right:
                    j += 1
                elif (i, j) == end:
                    break
                else:
                    assert False, "bad down-left move"
        return arr


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
            ],
            [1, 2, 6, 7, 3, 4, 8, 9, 5, 10],
        ),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
    ]
    for (mat, solution) in tests:
        result = sol.findDiagonalOrder(mat)
        assert result == solution, f"result {result} != solution {solution}"
    print("✅ All tests passed")

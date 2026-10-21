# https://leetcode.com/problems/rotate-image

"""
Notes:
    - Somewhat straight forward intuition, just a lot of nitty gritty
      details in terms of getting the iteration bounds set between the
      two loops, and how to index the 4 swap elements as a functon of
      the `i` and `j` values
    - Not sure if there's much to make this faster or easier, other than
      just "think about it" and/or add some print debugging as you go.
    - Writing out an example like this helped me:

        example on 3x3 matrix:
        matrix[0, 0] -> matrix[0, 2]
        matrix[0, 2] -> matrix[2, 2]
        matrix[2, 2] -> matrix[2, 0]
        matrix[2, 0] -> matrix[0, 0]

        generalized
        matrix[i,j] -> matrix[j, end - i]
        matrix[j, end - i] -> matrix[end - i, end - j]
        matrix[end - i, end - j] -> matrix[end - j, i]
        matrix[end - j, i] -> matrix[i, j]
"""

class Solution(object):
    def pretty_matrix(self, matrix):
        lines = []
        lines.append("[")
        for row in matrix:
            lines.append(str(row))
        lines.append("]")
        s = "\n".join(lines) + "\n"
        return s

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        assert len(matrix) == len(matrix[0]), "matrix not square"
        n = len(matrix)
        end = n - 1
        for i in range(n):
            for j in range(i, end - i):
                # note: technially this is possible with a single `tmp`
                # holder variable, but its hella confusing. this
                # solution is still constant in extra space.
                top = matrix[i][j]
                right = matrix[j][end - i]
                bottom = matrix[end - i][ end - j]
                left = matrix[end - j][i]

                # top -> right
                matrix[j][end - i] = top
                # right -> bottom
                matrix[end - i][end - j] = right
                # bottom -> left
                matrix[end - j][i] = bottom
                # left -> top
                matrix[i][j] = left

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1,2,3],[4,5,6],[7,8,9]],
             [[7,4,1],[8,5,2],[9,6,3]],
        ),
        (
            [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
            [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
        )
    ]
    for (matrix, solution) in tests:
        sol.rotate(matrix)
        assert matrix == solution, \
            f"matrix {sol.pretty_matrix(matrix)} != solution {sol.pretty_matrix(solution)}"
    print("✅ All tests passed")


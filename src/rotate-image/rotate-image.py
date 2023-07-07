# https://leetcode.com/problems/rotate-image

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                # print(f"{matrix[i][j]} ", end='')
                x = j
                y = cols - i - 1
                tmp = matrix[x][y]
                print(f"{matrix[x][y]} ", end='')
            print("")
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ],
            [
                [7,4,1],
                [8,5,2],
                [9,6,3]
            ]
        ),
        (
            [
                [5,1,9,11],
                [2,4,8,10],
                [13,3,6,7],
                [15,14,12,16],
            ],
            [
                [15,13,2,5],
                [14,3,4,1],
                [12,6,8,9],
                [16,7,10,11]
            ]
        )
    ]
    for (matrix, solution) in tests:
        result = sol.rotate(matrix)
        # assert
    # print("✅ All tests passed")


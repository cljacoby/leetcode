# https://leetcode.com/problems/pascals-triangle-ii

# [1],
# [1,1],
# [1,2,1],
# [1,3,3,1],
# [1,4,6,4,1],

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(1, rowIndex+1):
            tmp = []
            for j in range(len(row) + 1):
                a = row[j-1] if j-1 >= 0 else 0
                b = row[j] if j < len(row) else 0
                tmp.append(a+b)
            row = tmp
        return row
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (3, [1,3,3,1]),
        (0, [1]),
        (1, [1,1]),
        (4, [1,4,6,4,1]),
    ]
    for (row_idx, solution) in tests:
        result = sol.getRow(row_idx)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


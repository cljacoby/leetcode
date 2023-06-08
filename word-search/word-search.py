# https://leetcode.com/problems/word-search

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        for i, row in enumerate(self.board):
            for j, _cell in enumerate(row):
                if self._step(0, set(), i, j):
                    return True
        return False

    def _step(self, pos, seen, i, j):
        if (
            pos >= len(self.word)
            or (i,j) in seen
            or i < 0
            or j < 0
            or i >= len(self.board)
            or j >= len(self.board[0])
            or self.word[pos] != self.board[i][j]
        ):
            return False
        if pos == len(self.word) - 1:
            return True
        seen.add((i,j))
        res = self._step(pos + 1, seen, i + 1, j) \
            or self._step(pos + 1, seen, i - 1, j) \
            or self._step(pos + 1, seen, i, j + 1) \
            or self._step(pos + 1, seen, i, j - 1)
        seen.remove((i,j))
        return res


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "SEE",
            True,
        ),
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
            False,
        ),
    ]
    for (i, (board, word, solution)) in enumerate(tests):
        result = sol.exist(board, word)
        assert result == solution, f"test {i}: result {result} != solution {solution}"
    print("✅ All tests passed")

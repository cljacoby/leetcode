# https://leetcode.com/problems/word-search

'''
Key Insights:
    - Pretty straightforward intuition
    - Essentially got it first try, missed the `if (i, j) not in path`
      check, but immediately realized the mistake using the initial
      provided test cases. Just should have double checked.
    - I submitted it to claude and confirmed the ideal algorithmic
      complexity. Claude suggested the pruning optimizations of
      confirming `word` fits on `board`, the character counts of
      `word` or less than or equal to those in `board`
'''

from collections import Counter

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        self.n = len(self.board)
        self.m = len(self.board[0])

        ## cheap tricks
        # 1. check word actually fits on board
        if len(self.word) > self.m * self.n:
            return False
        # 2. check if the char frequencies of `word` are <= char frequencies of `board`
        if not self.char_check():
            return False
        # 3. Orient word so the rarer beginning or end char is first,
        #    i.e. potentially reverse the word
        self.maybe_rev_word()

        path = set()
        for (i, row) in enumerate(self.board):
            for (j, char) in enumerate(row):
                if self.try_word(0, path, i, j):
                    return True
        return False

    def try_word(self, idx, path, i, j):
        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            return False
        if self.board[i][j] != self.word[idx]:
            return False
        if (i, j) in path:
            return False
        if idx == len(self.word) - 1:
            return True
        path.add((i, j))
        b = (
               self.try_word(idx + 1, path, i + 1, j)
            or self.try_word(idx + 1, path, i, j + 1)
            or self.try_word(idx + 1, path, i - 1, j) 
            or self.try_word(idx + 1, path, i, j - 1)
        )
        path.remove((i, j))
        return b

    def char_check(self):
        freq_word = Counter(self.word)
        freq_board = sum([Counter(row) for row in self.board], Counter())
        return freq_word <= freq_board

    def maybe_rev_word(self):
        # note: could refactor the pruning checks with `char_check` to
        # avoid the double init of `freq_board`
        freq_board = sum([Counter(row) for row in self.board], Counter())
        if freq_board[self.word[0]] > freq_board[self.word[-1]]:
            # note: equivalent to `self.word = "".join(reversed(self.word))`
            self.word = self.word[::-1]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCCED",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "SEE",
            True,
        ),
        (
            [
                ["A", "B", "C", "E"],
                ["S", "F", "C", "S"],
                ["A", "D", "E", "E"],
            ],
            "ABCB",
            False,
        ),
    ]
    for (board, word, solution) in tests:
        result = sol.exist(board, word)
        assert result == solution, \
            f"result {result} != solution {solution}, word {word}, board {board}"
    print("✅ All tests passed")


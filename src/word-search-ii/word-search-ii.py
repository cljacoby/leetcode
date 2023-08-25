# https://leetcode.com/problems/word-search-ii

from collections import defaultdict
import json

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        solutions = set()
        first_chars = defaultdict(list)
        for i, word in enumerate(words):
            first_chars[word[0]].append(i)
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                char = board[i][j]
                idxs = first_chars.get(char)
                if idxs == None:
                    continue
                for idx in idxs:
                    word = words[idx]
                    if word in solutions:
                        continue
                    if self.step(board, i, j, 0, word, set()):
                        solutions.add(word)
        return list(solutions)

    def step(self, board, i, j, idx, word, seen):
        # print(f"step(), i={i}, j={j}, idx={idx}, word={word}")
        if (
            i < 0
            or j < 0
            or i >= len(board)
            or j >= len(board[0])
            or word[idx] != board[i][j]
            or (i,j) in seen
        ):
            return False
        nxt = idx + 1
        if nxt == len(word):
            return True
        seen.add((i,j))
        res = (
            self.step(board, i + 1, j, nxt, word, seen)
            or self.step(board, i - 1, j, nxt, word, seen)
            or self.step(board, i, j + 1, nxt, word, seen)
            or self.step(board, i, j - 1, nxt, word, seen)
        )
        seen.remove((i,j))
        return res


if __name__ == "__main__":
    sol = Solution()
    d = json.load(open("test1.json"))
    tests = [
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
        ),
        (
            [
                ["a","b","c"],
                ["a","e","d"],
                ["a","f","g"]
            ],
            ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"],
            # ["eaabcdgfa"],
            ["abcdefg","befa","eaabcdgfa","gfedcbaaa"],
        ),
        (
            [["a", "b"], ["c", "d"]],
            ["abcb"],
            [],
        ),
        (
            d['board'],
            d['words'],
            d['solution'],
        ),

    ]
    for (board, words, solution) in tests:
        result = sol.findWords(board, words)
        assert set(solution) == set(result), \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

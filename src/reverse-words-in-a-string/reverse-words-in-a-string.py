#  https://leetcode.com/problems/reverse-words-in-a-string

from collections import deque

class Solution(object):
    def flush(self, words, word):
        if len(word) == 0:
            return
        s = ""
        while len(word) > 0:
            s += word.pop()
        words.append(s)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        words = list()
        word = list()
        while len(s) > 0:
            char = s.pop()
            if char == " ":
                self.flush(words, word)
            else:
                word.append(char)
        self.flush(words, word)
        return " ".join(words)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            "one two three",
            "three two one",
        ),
        (
            "",
            "",
        ),
        (
            "  hello world  ",
            "world hello",
        )
    ]
    for (s, solution) in tests:
        result = sol.reverseWords(s)
        assert result == solution, \
            f"result \"{result}\" != solution \"{solution}\""
    print("✅ All tests passed")


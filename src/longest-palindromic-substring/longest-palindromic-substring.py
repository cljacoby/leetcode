# https://leetcode.com/problems/longest-palindromic-substring

# Trying out using 2 pointer directly instead of a deque.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.length = len(s)
        self.max = 1
        self.out = s[0]
        for i in range(self.length):
            self.step(s, i, i)
            self.step(s, i, i + 1)
        return self.out

    def step(self, s, i, j):
        while (
            i >= 0
            and j < self.length
            and s[i] == s[j]
        ):
            l = j - i + 1
            if l > self.max:
                self.max = l
                self.out = s[i:j+1]
            i -= 1
            j += 1

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("babad", ["aba", "bab"]),
        ("cbbd", ["bb"]),
        ("bb", ["bb"])
    ]
    for (s, solutions) in tests:
        result = sol.longestPalindrome(s)
        assert result in solutions, \
            f"result {result} not in solutions {solutions}"
    print("✅ All tests passed")


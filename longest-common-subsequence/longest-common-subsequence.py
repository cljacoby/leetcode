# https://leetcode.com/problems/longest-common-subsequence

# Did this python implementation as a sanity check when I was running
# into trouble with the rust implementation. There otherwise 1:1
# duplicate implementations in the respective languages.
class Solution(object):
    def longestCommonSubsequence(self, s1, s2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        return self.step(0, 0, s1, s2, dict())

    def step(self, i, j, s1, s2, cache):
        if i == len(s1) or j == len(s2):
            return 0
        if (i,j) in cache:
            return cache[(i,j)]
        n = None
        if s1[i] == s2[j]:
            n = 1 + self.step(i + 1, j + 1, s1, s2, cache)
        else:
            n = max(
                self.step(i + 1, j, s1, s2, cache),
                self.step(i, j + 1, s1, s2, cache),
            )
        cache[(i,j)] = n
        return cache[(i,j)]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("bl", "yby", 1),
        ("pmjghexybyrgzczy", "hafcdqbgncrcbihkd", 4),

    ]
    for (s1, s2, solution) in tests:
        result = sol.longestCommonSubsequence(s1, s2)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return "".join(word1) == "".join(word2)
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["ab", "c"],["a", "bc"], True),
        (["a", "cb"],["ab", "c"], False),
    ]
    for (w1, w2, solution) in tests:
        result = sol.arrayStringsAreEqual(w1, w2)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


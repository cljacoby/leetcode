# https://leetcode.com/problems/find-common-characters

class Solution(object):
    def counts(self, word):
        d = dict()
        for char in word:
            d[char] = d.get(char, 0) + 1
        return d

    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        common, words = self.counts(words[0]), words[1:]
        for word in words:
            counts = self.counts(word)
            keys = common.keys() & counts.keys()
            common = { k: min(common[k], counts[k]) for k in keys }
        s = []
        for (char, count) in common.items():
            s.extend([char] * count)
        return s

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            ["bella","label","roller"],
            ["e","l","l"],
        ),
        (
            ["cool","lock","cook"],
            ["c","o"],
        )
    ]
    for (words, solution) in tests:
        result = sol.commonChars(words)
        assert sorted(result) == sorted(solution), \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


# https://leetcode.com/problems/word-break

# Pretty easy, probs start to finish done in 10-15 mins. Only mistake I
# made was trying to using string.replace when I only wanted to replace
# the prefix.
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.word_dict = wordDict
        self.cache = dict()
        return self.step(s)

    def step(self, s):
        print(f"enter step. s={s}")
        if s == "":
            return True
        if s in self.cache:
            return self.cache[s]
        out = False
        for word in self.word_dict:
            size = len(word)
            if s[0:size] == word:
                new = s[size:]
                if self.step(new):
                    out = True
                    break
        self.cache[s] = out
        return self.cache[s]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("leetcode",  ["leet","code"], True),
        ("applepenapple",  ["apple","pen"], True),
        ("catsandog",  ["cats","dog","sand","and","cat"], False),
        ("catskicatcats", ["cats","cat","dog","ski"], True),
    ]
    for (s, words, solution) in tests:
        result = sol.wordBreak(s, words)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


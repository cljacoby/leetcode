# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

class Solution(object):

    def good_word(self, word, counts):
        for char in word:
            if char not in counts:
                return False
            counts[char] -= 1
            if counts[char] == 0:
                del counts[char]
        return True

    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        counts = dict()
        length = 0
        for char in chars:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        for word in words:
            if self.good_word(word, counts.copy()):
                length += len(word)
        return length

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["cat","bt","hat","tree"], "atach", 6),
        (["hello","world","leetcode"], "welldonehoneyr", 10),
    ]
    for (words, chars, solution) in tests:
        result = sol.countCharacters(words, chars)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


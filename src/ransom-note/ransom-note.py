# https://leetcode.com/problems/ransom-note

from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = defaultdict(int)
        for char in magazine:
            d[char] += 1
        for char in ransomNote:
            if char not in d:
                return False
            d[char] -= 1
            if d[char] == 0:
                del d[char]
        return True

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("aa", "aab", True),
        ("ab", "aa", False),
        ("cbab", "abbc", True),
    ]
    for (ransom, magazine, solution) in tests:
        result = sol.canConstruct(ransom, magazine)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


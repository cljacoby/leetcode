# https://leetcode.com/problems/roman-to-integer

class Solution(object):
    char_vals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    prefix = {
        "I": {"V", "X"},
        "X": {"L", "C"},
        "C": {"D", "M"},
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        idx = 0
        tot = 0
        while idx < len(s):
            char = s[idx]
            idx += 1
            if (
                char in self.prefix
                and idx < len(s)
                and s[idx] in self.prefix[char]
            ):
                nxt = s[idx]
                idx += 1
                tot += self.char_vals[nxt] - self.char_vals[char]
            else:
                tot += self.char_vals[char]
        return tot


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ]
    for (s, solution) in tests:
        result = sol.romanToInt(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

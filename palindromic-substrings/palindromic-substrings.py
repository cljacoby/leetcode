# https://leetcode.com/problems/palindromic-substrings

# Needed help with this one. Implementation is actually very simple,
# just was lost trying to generate all substr permutations as the base.
# 
# Key observation 1: Start at each string index. Assess if the current
# slice is a palindrome (i.e. outer left == outer right). If it is,
# decrement left index and increment right index. Repeat assessment
# until an index bounds violation, or palindromic assessment breaks.
# 
# Key observation 2: You have to start each palindrome both from a
# single index (i.e. left = right = 3), as well as from 2 adjacent
# indices (i.e. left = 3, right = 4). This is to account for palindromes
# which have an even length overall, and therefore not a singular middle
# position.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for (i, _char) in enumerate(s):
            count += self.step(s, i, i)
            count += self.step(s, i, i + 1)
        return count

    def step(self, s, left, right):
        count = 0
        while (
            left >= 0
            and right < len(s)
            and s[left] == s[right]
        ):
            left -= 1
            right += 1
            count += 1 
            print(f"count={count}, left={left}, right={right}, palindrome={s[left:right]}")
        return count

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abc", 3),
        ("aaa", 6),
        ("addaccadbabdbdbdbcabdcbcadacccbdddcbddacdaacbbdcbdbccdaaddadcaacdacbaaddbcaadcdab", 126)
    ]
    for (s, solution) in tests:
        result = sol.countSubstrings(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


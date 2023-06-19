# https://leetcode.com/problems/longest-repeating-character-replacement


# Overall a pretty simple problem, but needed some help on the
# intiution. I'm  realizing these sliding-window / 2-pointer questions
# are ones I probz need more practice in.
#
# 2 key observations
#
# Substr length:
#  At every iteration, you are considering the window running from the
#  left index, up to *and including* the right index. This means doing:
#    right - left + 1
#  And I was missing the +1
#
# Assessment:
#   Assess if the current substr can have K substitutions to
#   make is a single uniform character. The intiution here is
#   that if you subtract the count of the most frequent
#   character from the total substr length and the difference
#   is less than or equal to K, then it means you have enough
#   free operations to change every other remaining character
#   to match the most frequent character.
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = dict()
        left = 0
        longest = 0
        for right in range(len(s)):
            char = s[right]
            d[char] = d.get(char, 0) + 1
            # Get length of current window. Add 1 because its the length
            # of the substring up to and including element at `right`.
            substr_len = right - left + 1
            # Note: Make "Assessment", see note above for more info.
            if substr_len - max(d.values()) <= k:
                longest = max(longest, substr_len)
            else:
                last = s[left]
                d[last] -= 1
                if d[last] == 0:
                    del d[last]
        return longest

# Wrote a second solution to verify I understand the problem. This is
# probably slower, and definitely consumes more memory, but I think is a
# more intuitive solution, and bares a resemblance to the problem
# "longest-substring-without-repeating-characters". That problem
# combines the behaviors of a queue and a set, whereas this ones
# combines a queue and a hashmap.
from collections import deque
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = dict()
        substr = deque()
        longest = 0
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            substr.append(char)
            if len(substr) - max(freq.values()) <= k:
                longest = max(longest, len(substr))
            else:
                out = substr.popleft()
                freq[out] -= 1
        return longest


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("AABABBA", 1, 4),
        ("ABAB", 2, 4),
    ]
    for (s, k, solution) in tests:
        print("****************************")
        print(f"s={s}")
        result = sol.characterReplacement(s, k)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


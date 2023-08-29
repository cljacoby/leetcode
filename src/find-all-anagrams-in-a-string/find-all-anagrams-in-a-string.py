# https://leetcode.com/problems/find-all-anagrams-in-a-string

'''
TODO:
    - Try a solution using 2 pointers + HasMap (not Counter) to verify
      that I understand how to write it without the conveniance data
      structures.
'''

from collections import deque, Counter

# Deque + HashMap (i.e. Counter) solution
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        d = deque()
        length = len(p)
        c1 = Counter()
        c2 = Counter(p)
        solutions = list()
        for i, char in enumerate(s):
            d.append(char)
            c1[char] += 1
            if c1.total() > length:
                out = d.popleft()
                c1[out] -= 1
                if c1[out] == 0:
                    del c1[out]
            if c1 == c2:
                solutions.append(i - length + 1)
        return solutions

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("cbaebabacd", "abc", [0,6]),
        ("abab", "ab", [0,1,2]),
    ]
    for (s, p, solution) in tests:
        result = sol.findAnagrams(s, p)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters

from collections import deque

def empty(q):
    return len(q['a']) == 0 or len(q['b']) == 0 or len(q['c']) == 0

def upnext(q):
    tri = min(
        (q['a'][0], 'a', ('b', 'c')),
        (q['b'][0], 'b', ('a', 'c')),
        (q['c'][0], 'c', ('a', 'b')),
        key=lambda tri: tri[0]
    )
    return tri

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = {
            'a': deque([]),
            'b': deque([]),
            'c': deque([]),
        }
        for i, char in enumerate(s):
            q[char].append(i)
        size = len(s)
        count = 0
        while not empty(q):
            _i, x, (y, z) = upnext(q)
            j = max(q[y][0], q[z][0])
            count += size - j
            q[x].popleft()
        return count

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("aaacb", 3),
        ("abcabc", 10),
        ("acbbcac", 11),
    ]
    for (s, solution) in tests:
        result = sol.numberOfSubstrings(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


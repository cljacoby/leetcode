# https://leetcode.com/problems/sort-characters-by-frequency

from heapq import heappush, heappop
from collections import defaultdict

# Priority Queue implementation. O(n* log(n)). Requires 2 passes over
# input.
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = defaultdict(int)
        pq = []
        for char in s:
            counts[char] += 1
        for char, count in counts.items():
            heappush(pq, (-1 * count, char))
        s = ""
        while len(pq) > 0:
            count, char = heappop(pq)
            count *= -1
            s += char * count
        return s

# Priority Queue implementation. O(n* log(n)). Done in 1 pass; however,
# will have additional overhead of skipping stale elements in Priortiy Queue.
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = defaultdict(int)
        pq = []
        for char in s:
            counts[char] += 1
            heappush(pq, (-1 * counts[char], char))
        s = ""
        while len(pq) > 0:
            count, char = heappop(pq)
            count *= -1
            if count != counts[char]:
                continue
            s += char * count
        return s

# HashMap + Sort using python builtin sorted(). O(n * logn).
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        itr = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        s = ""
        res = []
        for (char, count) in itr:
            s += char * count
        return s


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("cccaaa", "aaaccc"),
        ("Aabb", "bbAa")
    ]
    for (s, solution) in tests:
        result = sol.frequencySort(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


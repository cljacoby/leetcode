# https://leetcode.com/problems/count-number-of-homogenous-substrings

from collections import deque

# Using a double ended queue. More intuitive to think about (imo).
class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = deque()
        count = 0
        for char in s:
            while len(q) > 0 and q[0] != char:
                q.popleft()
            q.append(char)
            count += len(q)
        return count % (pow(10, 9) + 7)

# Using 2 pointers. Slightly less intuitive, although basically same
# solution as above. Doesn't require extra memory for the queue.
class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = count = 0
        for char in s:
            while right - left > 0 and s[left] != char:
                left += 1
            right += 1
            count += right - left
        return count % (pow(10, 9) + 7)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("abbcccaa", 13),
        ("xy", 2),
        ("zzzzz", 15),
    ]
    for (s, solution) in tests:
        result = sol.countHomogenous(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


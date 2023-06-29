# https://leetcode.com/problems/insert-interval

from collections import deque

class Solution(object):

    def insert(self, intervals, new):
        """
        :type intervals: List[List[int]]
        :type new: List[int]
        :rtype: List[List[int]]
        """
        left = []
        right = []
        q = deque(intervals)
        start, end = new[0], new[1]
        while len(q) > 0:
            pair = q.popleft()
            if pair[1] < start:
                left.append(pair)
            elif pair[0] > end:
                right.append(pair)
            else:
                start = min(start, pair[0])
                end = max(end, pair[1])
        out = left + [[start, end]] + right
        return out

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1,3],[6,9]],
            [2,5],
            [[1,5],[6,9]],
        ),
        (
            [[1,2],[3,5],[6,7],[8,10],[12,16]],
            [4,8],
            [[1,2],[3,10],[12,16]],
        ),
        (
            [[1,5]],
            [2,7],
            [[1,7]]
        ),
    ]
    for (intervals, new, solution) in tests:
        result = sol.insert(intervals, new)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


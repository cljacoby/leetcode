# https://leetcode.com/problems/find-minimum-t-to-reach-last-room-i

from collections import deque

class Solution(object):
    HOPS = [
        (1, 0),        # up 
        (0, 1),        # right
        (-1, 0),       # down
        (0, -1),       # left
    ]

    def minTimeToReach(self, move_t):
        """
        :type move_t: List[List[int]]
        :rtype: int
        """
        n = len(move_t)
        m = len(move_t[0])
        q = deque([(0, 0, 0)])
        seen = set()
        mn = float('inf')
        while len(q) > 0:
            (x, y, t) = q.popleft()
            if (x < 0
                or y < 0
                or x >= n
                or y >= m
                or (x, y) in seen
            ):
                continue
            # print(f"pop. pos=({x},{y}), t={t}")
            if x == n - 1 and y == m - 1:
                mn = min(mn, t)
                continue
            seen.add((x, y))
            for dx, dy in self.HOPS:
                i, j = x + dx, y + dy
                tnew = max(t, move_t[x][y]) + 1
                q.append((i, j, tnew))
        return mn

if __name__ == "__main__":
    sol = Solution()
    tests = [
        # ([[0,4],[4,4]], 6),
        # ([[0,0,0],[0,0,0]], 3),
        ([[15,58],[67,4]], 60),
    ]
    for (move_t, solution) in tests:
        result = sol.minTimeToReach(move_t)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


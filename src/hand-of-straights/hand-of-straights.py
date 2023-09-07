# https://leetcode.com/problems/hand-of-straights

from collections import deque

class Solution(object):
    def isNStraightHand(self, hand, size):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if not len(hand) % size == 0:
            return False
        q = deque(sorted(hand))
        n_buckets = len(hand) // size
        buckets = [[] for _ in range(n_buckets)]
        b = 0
        reque = []
        while len(q) > 0:
            n = q.popleft()
            if (
                len(buckets[b]) == 0
                or buckets[b][-1] == n - 1
            ):
                buckets[b].append(n)
                if len(buckets[b]) == size:
                    while len(reque) > 0:
                        q.appendleft(reque.pop())
                    b += 1
            else: 
                reque.append(n)
        return len(reque) == 0

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,3,6,2,3,4,7,8],
            3,
            True,
        ),
        (
            [1,2,3,4,5],
            4,
            False,
        ),
        (
            [8,10,12],
            3,
            False,
        ),
    ]
    for (hand, size, solution) in tests:
        result = sol.isNStraightHand(hand, size)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


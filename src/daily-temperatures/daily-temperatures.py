# https://leetcode.com/problems/daily-temperatures

from heapq import heappush, heappop

# Solution with heap queue. First solution that occurred to me.
# From looking at accepted solutions, a simple stack would
# have also sufficed.
class Solution(object):
    def dailyTemperatures(self, temps):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        heap = []
        solution = [0] * len(temps)
        for i, t in enumerate(temps):
            while len(heap) > 0 and heap[0][0] < t:
                _, j = heappop(heap)
                solution[j] = i - j
            heappush(heap, (t, i))
        return solution


# Essentially same implementation as above; however, data structure of
# choice is a simple stack. This should be faster as appending to a
# stack is quicker than appending to a heap, as the heap needs to be
# re-balanced to maintain the heap property.
class Solution(object):
    def dailyTemperatures(self, temps):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        solution = [0] * len(temps)
        for i, t in enumerate(temps):
            while len(stack) > 0 and stack[-1][1] < t:
                (j, _) = stack.pop()
                solution[j] = i - j
            stack.append((i, t))
        return solution

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [73, 74, 75, 71, 69, 72, 76, 73],
            [1, 1, 4, 2, 1, 1, 0, 0]
        ),
        (
            [30, 40, 50, 60],
            [1, 1, 1, 0],
        ),
        (
            [30, 60, 90],
            [1, 1, 0]
        ),
    ]
    for (temps, solution) in tests:
        result = sol.dailyTemperatures(temps)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

# https://leetcode.com/problems/merge-intervals

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        pairs = sorted(intervals, key=lambda pair: pair[0], reverse=True)
        merged = []
        while len(pairs) > 0:
            pair = pairs.pop()
            if len(merged) == 0:
                merged.append(pair)
                continue
            last = merged[-1]
            if pair[0] > last[1]:
                merged.append(pair)
            else:
                start = last[0]
                end = max(last[1], pair[1])
                merged[-1] = [start, end]
        return merged


        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
        ([[4,7],[1,4]], [[1,7]]),
    ]
    for (pairs, solution) in tests:
        result = sol.merge(pairs)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


# https://leetcode.com/problems/non-overlapping-intervals

# First attempt. Idea was to basically store the counts of the observed
# indices, incrementing when an interval was opened an decrementing when
# an interval was closed. This seems to capture intervals conflicting on
# the same indices, but does not capture overlapping intervals with all
# unique indices.
class _Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        d = dict()
        for pair in intervals:
            start, end = tuple(pair)
            if start not in d:
                d[start] = 0
            if end not in d:
                d[end] = 0
            d[start] += 1
            d[end] -= 1
        s = [v for (k,v) in sorted(d.items(), key=lambda pair: pair[0])]
        peak = tot = 0
        for i in s:
            tot += i
            peak = max(tot, peak)
        print(f"d={d}")
        print(f"s={s}")
        print(f"peak={peak}, tot={tot}")
        return peak - 1

# Had to get some help from other submissions to get this solution.
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        # The last interval's ending index. Init to min value from problem statement.
        prev = -1 * pow(10, 5)

        # Sort on start time.
        intervals.sort(key=lambda pair: pair[0])

        # Count of interval conflicts
        count = 0
        
        for (start, end) in intervals:
            if start >= prev:
                # No interval conflict. Update prev for next comparison.
                prev = end
            else:
                # Interval conflict. Select interval with lower end
                # time, as the bigger range will always have more
                # potential future conflicts. 
                count += 1
                prev = min(prev, end)
        return count

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0),
        ([[0,1],[3,4],[1,2]], 0),
        ([[0,2],[1,3],[2,4],[3,5],[4,6]], 2),
    ]
    for (intervals, solution) in tests:
        result = sol.eraseOverlapIntervals(intervals)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


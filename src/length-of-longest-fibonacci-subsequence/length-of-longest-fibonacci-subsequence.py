# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence

class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        t = [[0 for j in range(n)]
                    for i in range(n)]
        val_to_idx = { x:i for i,x in enumerate(arr) }
        mx = 0

        for curr in range(n):
            for prev in range(curr):
                diff = arr[curr] - arr[prev]
                diff_idx = val_to_idx.get(diff, -1)
                if (
                    diff in val_to_idx
                    and diff_idx < prev
                ):
                    diff_idx = val_to_idx[diff]
                    t[prev][curr] = max(t[diff_idx][prev] + 1, 3)
                    mx = max(t[prev][curr], mx)
        return mx
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
             [1,2,3,4,5,6,7,8],
             5,
        ),
        (
            [1,3,7,11,12,14,18],
            3,
        ),
        (
            [2,4,7,8,9,10,14,15,18,23,32,50],
            5,
        ),
    ]
    for (arr, solution) in tests:
        result = sol.lenLongestFibSubseq(arr)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


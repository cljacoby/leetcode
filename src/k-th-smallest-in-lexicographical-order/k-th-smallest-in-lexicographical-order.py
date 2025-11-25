# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ret = [1]
        curr = 1
        while len(ret) < n:
            while curr * 10 <= n:
                curr *= 10
                ret.append(curr)
                if len(ret) == n + 1:
                    return ret[-1]
                continue
            curr += 1
            if curr % 10 != 0:
                if curr <= n:
                    ret.append(curr)
                    if len(ret) == n + 1:
                        return ret[-1]
                continue
            while curr % 10 == 0:
                curr //= 10
            ret.append(curr)
            if len(ret) == n + 1:
                return ret[-1]
        return ret[k-1]

        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (13, 2, 10),
        (1, 1, 1),
    ]
    for (n, k, solution) in tests:
        result = sol.findKthNumber(n, k)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


# https://leetcode.com/problems/lexicographical-numbers

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = [1]
        curr = 1
        while len(ret) < n:
            while curr * 10 <= n:
                curr *= 10
                ret.append(curr)
                continue
            curr += 1
            if curr % 10 != 0 and curr <= n:
                ret.append(curr)
                continue
            while curr % 10 == 0:
                curr //= 10
                ret.append(curr)
        return ret
 

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (13, [1,10,11,12,13,2,3,4,5,6,7,8,9]),
    ]
    for (n, solution) in tests:
        result = sol.lexicalOrder(n)
        assert result == solution, \
                f"result {result} != solution {solution}"
    print("✅ All tests passed")


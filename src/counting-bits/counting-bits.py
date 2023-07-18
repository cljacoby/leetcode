# https://leetcode.com/problems/counting-bits

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Model as u32
        bits = [0] * 32
        last = len(bits) - 1
        ones = 0
        out = [0] 
        for num in range(1, n + 1):
            if bits[last] == 0:
                bits[last] = 1
                ones += 1
            else:
                j = last
                while bits[j] == 1:
                    bits[j] = 0
                    ones -= 1
                    j -= 1
                bits[j]  = 1
                ones += 1
            out.append(ones)
        return out

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (2, [0,1,1]),
        (5, [0,1,1,2,1,2]),
    ]
    for (n, solution) in tests:
        result = sol.countBits(n)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


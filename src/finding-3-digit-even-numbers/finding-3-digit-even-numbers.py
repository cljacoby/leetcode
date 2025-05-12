# https://leetcode.com/problems/finding-3-digit-even-numbers

'''
Trick is to regonize instead of trying to generate all 3 length
permutations of `digits`, the solution range is bounded from [100, 999].
So instead, iterate over each number in this range, see if the number
is:
    - positive
    - no leading zero
    - composable from original digits (hashmap char count compare)
Put all valid solutions into a list, and return.
'''

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        freq_all = self.freq(digits)
        mn = 100
        mx = 999
        solutions = []
        for x in range(mn, mx + 1):
            d = self.digits(x)
            f = self.freq(d)
            valid = self.valid(d, f, freq_all)
            # print("x={x}, d={d}, freq={freq}, valid={valid}")
            if valid:
                solutions.append(x)
        return solutions


    def valid(self, digits, freq, freq_all):
        if digits[0] == 0:
            return False
        if digits[-1] % 2 != 0:
            return False
        for dig in digits:
            if dig not in freq_all or freq[dig] > freq_all[dig]:
                return False
        return True
 
    def digits(self, x):
        rem = x
        digits = []
        while rem > 0:
            digit = rem % 10
            digits.append(digit)
            rem = (rem - digit) // 10
        return list(reversed(digits))

    def freq(self, arr):
        freq = dict()
        for dig in arr:
            if dig not in freq:
                freq[dig] = 0
            freq[dig] += 1
        return freq
 

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2,1,3,0], [102,120,130,132,210,230,302,310,312,320]),
        ([2,2,8,8,2], [222,228,282,288,822,828,882]),
    ]
    for (digits, solution) in tests:
        result = sol.findEvenNumbers(digits)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


# https://leetcode.com/problems/largest-3-same-digit-number-in-string

from collections import deque, Counter
class _Solution(object):
    def largestGoodInteger(self, s):
        """
        :type num: str
        :rtype: str
        """
        window = deque()
        counts = Counter()
        mx = (float('-inf'), "")
        for char in s:
            x = int(char)
            window.append(x)
            counts[x] += 1
            if len(window) > 3:
                y = window.popleft()
                counts[y] -= 1
                if counts[y] == 0:
                    del counts[y]
            if len(window) == 3 and len(counts) == 1:
                win_str = f"{window[0]}{window[1]}{window[2]}"
                win_num = int(win_str)
                if win_num > mx[0]:
                    mx = (win_num, win_str)
        return mx[1]

# No conveniance data structures
class Solution(object):
    def largestGoodInteger(self, s):
        """
        :type num: str
        :rtype: str
        """
        counts = dict()
        mx = (float('-inf'), "")
        left = 0
        for right in range(len(s)):
            if s[right] in counts:
                counts[s[right]] += 1
            else:
                counts[s[right]] = 1
            if right - left == 3:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            if right - left == 2 and len(counts) == 1:
                win_str = s[left:right+1] 
                win_num = int(win_str)
                if mx[0] < win_num:
                    mx = (win_num, win_str)
        return mx[1]

# Dead simple way of doing it. I kind of overthought it with 2 pointers
# and sliding windows
class Solution(object):
    def largestGoodInteger(self, s):
        """
        :type num: str
        :rtype: str
        """
        mx = (-1, "")
        for i in range(2, len(s)):
            if s[i] == s[i-1] == s[i-2]:
                x = int(s[i])
                if x > mx[0]:
                    mx = (x, s[i] * 3)
        return mx[1]

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("6777133339", "777"),
        ("2300019", "000"),
        ("42352338", ""),
        ("3200014888", "888"),
    ]
    for (s, solution) in tests:
        result = sol.largestGoodInteger(s)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


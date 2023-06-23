# https://leetcode.com/problems/container-with-most-water

import json


# First attempt. I think this is closed but is degrading into hacks on
# hacks to try and pass all the various tests. Going to step back and
# re-assess.
class _Solution(object):
    def area(self, h, left, right):
        return (right - left) * min(h[left], h[right])

    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        max_area = self.area(h, left, right)
        length = len(h)
        
        for i in range(1, length):
            # Assess move left forward
            for j in range(left, right):
                area = self.area(h, j, right)
                if area > max_area:
                    max_area = area
                    left = j
            # Assess move right forward
            area = self.area(h, left, i)
            if area > max_area:
                right = i
                max_area = area
            print(f"i={i}, left={left}, right={right}, max_area={max_area}")
        return max_area

# Referenced accepted solutions for help. Key insight is you from widest
# possible range, and move inward each increment. I think the question I
# need to understand is with these problems, when is it appropriate to
# start wide and work inward, and when is it appropriate to use a
# sliding window?
class Solution(object):
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        # Start from widest array and move inward
        left = 0
        right = len(h) - 1
        area = 0
        while right > left:
            area = max(area, (right - left) * min(h[left], h[right])) 
            if h[right] > h[left]:
                left += 1
            else:
                right -= 1
        return area

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        (json.load(open("test1.json")), 92344),
        ([2,3,4,5,18,17,6], 17),
        ([0,14,6,2,10,9,4,1,10,3], 70),
        ([4,3,2,1,4], 16),
        ([0,2], 0),
    ]
    for (nums, solution) in tests:
        print("****************************")
        print(f"nums={nums}")
        result = sol.maxArea(nums)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


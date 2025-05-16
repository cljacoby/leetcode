# https://leetcode.com/problems/smallest-number-in-infinite-set

'''
Slightly better solution would be to use heapq instead of list(), set()
combination.
'''

class SmallestInfiniteSet(object):
    def __init__(self):
        self.next = 1
        self.re_add = [list(), set()]

    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.re_add[0]) > 0:
            out = self.re_add[0].pop()
            self.re_add[1].remove(out)
            return out
        out = self.next
        self.next += 1
        return out

    def _bisect_insert(self, num):
        """
        binary search re_add array, and insert in descending sorted order.
        """
        left = 0
        right = len(self.re_add[0])
        while left < right:
            mid = (right - left) // 2 + left
            if num < self.re_add[0][mid]:
                left = mid + 1
            else:
                right = mid
        self.re_add[0].insert(left, num)

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num >= self.next:
            return
        if num in self.re_add[1]:
            return
        self._bisect_insert(num)
        self.re_add[1].add(num)


if __name__ == "__main__":
    tests = [
        ["addBack",
            "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest",
            "addBack","addBack","addBack","addBack",
            "popSmallest", "popSmallest", "popSmallest", "popSmallest", "popSmallest", ],
        [[2],
            [], [], [], [], [],
            [1], [4], [2], [100],
            [], [], [], [], []],
        [None,
                1, 2, 3, 4, 5,
                None, None, None, None,
                1, 2, 4, 6, 7],
    ]
    sis = SmallestInfiniteSet()
    for (method, args, ret) in zip(tests[0], tests[1], tests[2]):
        f = getattr(sis, method)
        out = f(*args)
        assert out == ret, \
                f"out {out} != ret {ret}"
    print("✅ All tests passed")


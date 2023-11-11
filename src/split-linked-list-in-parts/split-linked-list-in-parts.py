# https://leetcode.com/problems/split-linked-list-in-parts

from ListNode import ListNode
import math

class Solution(object):

    def ll_len(self, head):
        l = 0
        while head != None:
            head = head.next
            l += 1
        return l

    def buckets(self, k, length):
        buckets = []
        while k > 0:
            b = math.ceil(length / k)
            buckets.append(b)
            length -= b
            k -= 1
        return buckets


    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length = self.ll_len(head)
        buckets = self.buckets(k, length)
        out = []
        for b in buckets:
            if b == 0:
                out.append(None)
            else:
                out.append(head)
                for i in range(b - 1):
                    head = head.next
                tmp = head.next
                head.next = None
                head = tmp
        return out
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,3,4,5,6,7,8,9,10],
            3,
            [[1,2,3,4],[5,6,7],[8,9,10]]
        ),
        (
            [1,2,3],
            5,
            [[1],[2],[3],[],[]]
        ),
    ]
    for (nums, k, solution) in tests:
        head = ListNode.from_array(nums)
        result = sol.splitListToParts(head, k)
        r = [ll.to_array() if ll != None else [] for ll in result]
        assert solution == r, \
            f"r {r} != solution {solution}, result={result}"
    print("✅ All tests passed")


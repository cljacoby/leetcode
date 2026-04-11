# https://leetcode.com/problems/merge-k-sorted-lists

from ListNode import ListNode

class Solution(object):

    def merge2Lists(self, n1, n2):
        head = tail = ListNode(val = "dummy")
        while n1 != None or n2 != None:
            if n1 == None:
                tail.next = n2
                tail = tail.next
                n2 = n2.next
                tail.next = None
            elif n2 == None or n1.val < n2.val:
                tail.next = n1
                tail = tail.next
                n1 = n1.next
                tail.next = None
            else:
                tail.next = n2
                tail = tail.next
                n2 = n2.next
                tail.next = None
        m = head.next
        return m

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return self.merge2Lists(lists[0], None)
        if len(lists) == 2:
            return self.merge2Lists(lists[0], lists[1])
        length = len(lists)
        mid = length // 2
        a = self.mergeKLists(lists[:mid])
        b = self.mergeKLists(lists[mid:])
        m = self.merge2Lists(a, b)
        return m
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[1,4,5],[1,3,4],[2,6]],
            [1,1,2,3,4,4,5,6],
        ),
        (
            [],
            [],
        ),
        (
            [[]],
            [],
        ),
    ]
    for (arrays, solution) in tests:
        lists  = [ListNode.from_array(arr) for arr in arrays]
        result = sol.mergeKLists(lists)
        print(f"lists = {lists}, result {result}, solution {solution}\n")
        # assert r == solution, \
        #     f"r {r} != solution {solution}, result={result}"
    # print("✅ All tests passed")


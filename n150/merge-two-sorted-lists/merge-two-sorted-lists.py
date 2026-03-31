# https://leetcode.com/problems/merge-two-sorted-lists

from ListNode import ListNode

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = tail = None
        n1, n2 = list1, list2
        while not (n1 == None and n2 == None):
            if n1 == None:
                n = n2
                n2 = n2.next
            elif n2 == None:
                n = n1
                n1 = n1.next
            elif n1.val < n2.val:
                n = n1
                n1 = n1.next
            else:
                n = n2
                n2 = n2.next
            if head == None:
                head = n
                tail = n
            else:
                tail.next = n
                tail = tail.next
            tail.next = None
        return head

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,4],
            [1,3,4],
            [1,1,2,3,4,4],
        ),
        (
            [0],
            [],
            [0],
        ),
        (
            [],
            [0],
            [0],
        ),
    ]
    for (n1, n2, solution) in tests:
        n1 = ListNode.from_array(n1)
        n2 = ListNode.from_array(n2)
        result = sol.mergeTwoLists(n1, n2)
        assert result.to_array() == solution, f"result {result} != solution {solution}"
    print("✅ All tests passed")


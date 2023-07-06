# https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from ListNode import ListNode

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        node = head
        while node != None:
            nid = id(node)
            if nid in seen:
                return True
            seen.add(nid)
            node = node.next
        return False

if __name__ == "__main__":
    sol = Solution()

    n0 = ListNode(0)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n0.next = n1
    n1.next = n2
    n2.next = n0
    
    m0 = ListNode.from_array([0,1,2,3,4,5])

    tests = [
        (n0, True),
        (m0, False)
    ]

    for (head, solution) in tests:
        result = sol.hasCycle(head)
        assert result == solution
    print("✅ All tests passed")


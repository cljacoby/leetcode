# https://leetcode.com/problems/linked-list-cycle

from ListNode import ListNode

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        node = head
        while node != None:
            nid = id(node)
            if nid in visited:
                return True
            visited.add(nid)
            node = node.next
        return False
        

if __name__ == "__main__":
    sol = Solution()

    l1 = ListNode.from_array([3,2,0,-4])
    l1.next.next.next = l1.next

    l2 = ListNode.from_array([1,2])
    l2.next = l2

    tests = [
        (
            l1,
            True,
        ),
        (
            l2,
            True,
        ),
        (
            ListNode.from_array([1,2,3,4,5]),
            False
        )
    ]

    for (ll, solution) in tests:
        result = sol.hasCycle(ll)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


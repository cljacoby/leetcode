# https://leetcode.com/problems/remove-nth-node-from-end-of-list

from ListNode import ListNode
from collections import deque

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        node = head
        size = n + 1
        window = deque([], maxlen=size)
        while node != None:
            window.append(node)
            node = node.next
        if len(window) == n:
            # We're attempting to remove the first Node of the list.
            # Therefore, move head forward one.
            head = window[1]
        else:
            window[0].next = window[1].next
        return head

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3,4,5], 2, [1,2,3,5]),
        ([1,2], 1, [1]),
        ([1,2], 2, [2]),
        ([1], 1, []),
    ]
    for (nums, n, solution) in tests:
        head = ListNode.from_array(nums)
        result = sol.removeNthFromEnd(head, n)
        res = result.to_array() if result != None else []
        assert res == solution
    print("✅ All tests passed")


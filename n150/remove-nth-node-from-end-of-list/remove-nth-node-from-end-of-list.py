# https://leetcode.com/problems/remove-nth-node-from-end-of-list

from ListNode import ListNode
from collections import deque

class Solution(object):
    def removeNthFromEnd(self, head, n):
        stack = deque([])
        node = head
        while node != None:
            stack.append(node)
            # space optimization: deque nodes which won't be relevant
            # for the node removal
            if len(stack) > n + 1:
                stack.popleft()
            node = node.next
        assert(n <= len(stack)), "nth node exceeds list length"
        i = 0
        node = None
        tail = None
        while i < n:
            tail = node
            node = stack.pop()
            i += 1
        if len(stack) > 0:
            stack[-1].next = tail
            return head
        return tail

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,3,4,5],
            2,
            [1,2,3,5],
        ),
        (
            [1,2,3,4,5],
            1,
            [1,2,3,4],
        ),
        (
            [1,2,3,4,5],
            5,
            [2,3,4,5],
        ),
        (
            [1],
            1,
            [],
        ),
        (
            [1,2],
            1,
            [1],
        ),
        (
            [1,2],
            2,
            [2],
        ),
    ]
    for (nums, n, solution) in tests:
        head = ListNode.from_array(nums)
        solution = ListNode.from_array(solution)
        result = sol.removeNthFromEnd(head, n)
        l1 = result.to_array() if result else None
        l2 = solution.to_array() if solution else None
        assert l1 == l2, f"result={result}, solution={solution}"
    print("✅ All tests passed")



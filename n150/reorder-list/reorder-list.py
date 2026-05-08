# https://leetcode.com/problems/reorder-list

from ListNode import ListNode
from collections import deque

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        q = deque([])
        node = head
        while node != None:
            tmp = node.next
            node.next = None
            q.append(node)
            node = tmp
        tail = head = None
        front = True
        while len(q) > 0:
            node = q.popleft() if front else q.pop()
            front = not front
            if not tail:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
        return head
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [1,2,3,4],
            [1,4,2,3],
        ),
        (
            [1,2,3,4,5],
            [1,5,2,4,3],
        ),
    ]
    for (nums, solution) in tests:
        head = ListNode.from_array(nums)
        result = sol.reorderList(head)
        result = result.to_array()
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")


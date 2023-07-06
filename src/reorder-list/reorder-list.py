# https://leetcode.com/problems/reorder-list

from ListNode import ListNode
from collections import deque

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None:
            return None
        q = deque([])
        node = head.next
        while node != None:
            q.append(node)
            node = node.next
        prev = head
        end = True
        while len(q) > 0:
            if end:
                node = q.pop()
            else:
                node = q.popleft()
            prev.next = node
            prev = node
            end = not end
        prev.next = None
        return head

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3,4], [1,4,2,3]),
        ([1,2,3,4,5], [1,5,2,4,3])
    ]
    for (nums, solution) in tests:
        head = ListNode.from_array(nums)
        sol.reorderList(head)
        res = head.to_array()
        assert solution == res
    print("✅ All tests passed")


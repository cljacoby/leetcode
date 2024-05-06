# https://leetcode.com/problems/remove-nodes-from-linked-list

from ListNode import ListNode

class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        mx = -1
        while len(stack) > 0:
            node = stack.pop()
            node.rm = mx > node.val
            mx = max(mx, node.val)
        prev = None
        node = head
        while node:
            if not node.rm:
                prev = node
            elif prev == None:
                head = head.next
            else:
                prev.next = node.next
            node = node.next
        return head

# -------------------------------------------------------

from collections import deque

class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        q = deque([])
        node = head
        while node:
            q.append(node)
            node = node.next
        mx = -1
        for node in reversed(q):
            node.rm = mx > node.val
            mx = max(mx, node.val)
        prev = None
        while len(q) > 0:
            node = q.popleft()
            if not node.rm:
                prev = node
            elif node == head:
                head = head.next
            else:
                prev.next = node.next
        return head

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([5,2,13,3,8], [13,8]),
        ([1,1,1,1], [1,1,1,1]),
    ]
    for (arr, solution) in tests:
        ll = ListNode.from_array(arr)
        res = sol.removeNodes(ll)
        res_arr = res.to_array()
        print(f"result {res_arr}, solution {solution}")
        assert res_arr == solution, \
            f"result {res_arr} != solution {solution}"
    print("✅ All tests passed")


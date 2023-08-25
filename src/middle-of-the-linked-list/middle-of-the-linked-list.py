# https://leetcode.com/problems/middle-of-the-linked-list

from ListNode import ListNode
import math

'''
Key Insights:
    - Looks like integer division or math.ciel work different
      between python2.7 and python3.x. This solution fails 
      in Leetcode's *Python* lang choice, but works on *Python3*
'''

class Solution(object):
    def length(self, head):
        if head == None:
            return 0
        length = 1
        while head.next != None:
            head = head.next
            length += 1
        return length

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        length = self.length(head)
        if length % 2 == 0:
            mid = int(length / 2) + 1
        else:
            mid = math.ceil(length / 2)
        i = 1
        while i < mid:
            head = head.next
            i += 1
        return head

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,3,4,5], 3),
        ([1,2,3,4,5,6], 4),
        ([1], 1),
    ]
    for (arr, solution) in tests:
        ll = ListNode.from_array(arr)
        mid = sol.middleNode(ll)
        assert mid.val == solution, \
            f"mid.val {mid.val} != solution {solution}"
    print("✅ All tests passed")


# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ListNode import ListNode

# Allocates new list, i.e. not in-place re-arrangement
class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        node = dummy = ListNode(-1)
        n1, n2 = l1, l2
        while n1 != None or n2 != None:
            print(f"n1={n1}, n2={n2}")
            if n2 == None:
                node.next = ListNode(n1.val)
                n1 = n1.next
            elif n1 == None:
                node.next = ListNode(n2.val)
                n2 = n2.next
            elif n1.val <= n2.val:
                node.next = ListNode(n1.val)
                n1 = n1.next
            else:
                node.next = ListNode(n2.val)
                n2 = n2.next
            node = node.next
        return dummy.next

# In-place merging 
class Solution(object):
    def mergeTwoLists(self, n1, n2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not n1 or not n2:
            return n1 or n2
        dummy = node = ListNode(-1)
        while n1 and n2:
            if n1.val <= n2.val:
                node.next = n1
                n1 = n1.next
            else:
                node.next = n2 
                n2 = n2.next
            node = node.next
        node.next = n1 or n2 
        return dummy.next

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
    ]
    for (l1, l2, solution) in tests:
        l1 = ListNode.from_array(l1)
        l2 = ListNode.from_array(l2)
        solution = ListNode.from_array(solution)
        result = sol.mergeTwoLists(l1, l2)
        print(f"l1={l1}, l2={l2}, solution={solution}, result={result}")
        # assert
    print("✅ All tests passed")


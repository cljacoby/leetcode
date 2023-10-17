# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

from ListNode import ListNode

# First solution. Intuitive approach. Check list length, 
# then iterate back up list with an index, and cut out the middle node.
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        length = self.length(head)
        if length <= 1:
            return None
        mid = length // 2
        i = 0
        prev = None
        node = head
        while i < mid:
            prev = node
            node = node.next
            i += 1
        assert prev != None, f"Invariant broken. prev={prev}, i={i}, mid={mid}."
        prev.next = node.next
        return head
        

    def length(self, head):
        length = 0
        while head != None:
            length += 1
            head = head.next
        return length

# Solution using 2 pointers. One advances 1 node at a time (slow) and
# advances 2 nodes at a time (fast). When fast.next.next is None, slow
# will be just before the midpoint, and we can delete the node.
# Interestinly, according to LeetCode the first solution ran faster.
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(val=0, next=head)
        slow = fast = dummy
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return dummy.next

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,3,4,7,1,2,6], [1,3,4,1,2,6]),
        ([1,2,3,4], [1,2,4]),
        ([2,1], [2]),
    ]
    for (a1, a2) in tests:
        l1, l2 = ListNode.from_array(a1), ListNode.from_array(a2)
        sol.deleteMiddle(l1)
        a1, a2 = ListNode.to_array(l1), ListNode.to_array(l2)
        assert a1 == a2, \
            f"l1 {l1} != l2 {l2}"
    print("✅ All tests passed")


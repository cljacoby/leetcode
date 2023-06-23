# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        s = ""
        node = self
        first = True
        while node != None:
            if not first:
                s = s + "->"
            s = s + f"{node.val}"
            node = node.next
            first = False
        return s

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def from_array(nums):
        if len(nums) == 0:
            return []
        node = dummy = ListNode(-1)
        for n in nums:
            node.next = ListNode(n)
            node = node.next
        return dummy.next

# Definition for doubly-linked list.
class DoubleListNode(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = None
        self.next = next

    def __repr__(self):
        s = ""
        node = self
        first = True
        while node != None:
            if not first:
                s = s + "<->"
            s = s + f"{node.val}"
            node = node.next
            first = False
        return s

    def __str__(self):
        return self.__repr__()

    def to_array(self):
        arr = list()
        node = self
        while node != None:
            arr.append(node.val)
            node = node.next
        return arr

    @staticmethod
    def from_array(nums):
        if len(nums) == 0:
            return []
        node = dummy = ListNode(-1)
        for n in nums:
            node.next = ListNode(n)
            node = node.next
        return dummy.next


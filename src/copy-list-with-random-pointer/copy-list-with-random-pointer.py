# https://leetcode.com/problems/copy-list-with-random-pointer

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def __repr__(self):
        return f"{{ val={self.val}, rand={'Y' if self.random != None else 'N'}, id={id(self)} }}"

    def __str__(self):
        return self.__repr__()

# ========================================================================

class Solution(object):
    def copyRandomList(self, head):
        """
        :type h1: Node
        :rtype: Node
        """
        idx1, idx2 = dict(), dict()
        h1 = head
        dummy = prev = Node(0, next=None)
        i = 0
        while h1 != None:
            idx1[h1] = i
            node = Node(h1.val)
            idx2[i] = node
            prev.next = node
            prev = node
            i += 1
            h1 = h1.next
        h1 = head
        h2 = dummy.next
        while h1 != None:
            if h1.random != None:
                h2.random = idx2[idx1[h1.random]]
            h1 = h1.next
            h2 = h2.next
        return dummy.next

if __name__ == "__main__":
    # [[7,None],[13,0],[11,4],[10,2],[1,0]],
    
    n0 = Node(7)
    n1 = Node(13)
    n2 = Node(11)
    n3 = Node(10)
    n4 = Node(1)

    n1.random = n0
    n2.random = n4
    n3.random = n2
    n4.random = n0

    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    
    sol = Solution()
    h1 = n0
    h2 = sol.copyRandomList(n0)
    while h1 != None and h2 != None:
        assert (h1.val == h2.val
                and bool(h1.random) == bool(h2.random)
                and id(h1) != id(h2))
        h1, h2 = h1.next, h2.next
    print("✅ All tests passed")


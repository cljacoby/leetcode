# https://leetcode.com/problems/copy-list-with-random-pointer

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def __repr__(self):
        s = ""
        node = self
        first = True
        while node != None:
            if not first:
                s = s + " -> "
            random = node.random.val if node.random else None
            s = s + f"{{ val:{node.val}, random:{random} }}\n\t"
            node = node.next
            first = False
        return s

    def __str__(self):
        return self.__repr__()

    def to_array(self):
        arr = list()
        node = self
        while node != None:
            arr.append([node.val, node.random])
            node = node.next
        return arr

# Leetcode doesn't allow adding methods on the Node type
# @staticmethod
def from_array(tuples):
    node = dummy = Node(-1)
    nodes = []
    for (val, _random) in tuples:
        new = Node(val)
        nodes.append(new)
        node.next = new
        node = node.next
    for (node, (_val, random)) in zip(nodes, tuples):
        if random != None:
            node.random = nodes[random]
    return dummy.next

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        vals = []
        rand_idxs = []
        addr_to_idx = {}

        node = head
        idx = 0
        while node != None:
            vals.append(node.val)
            addr = id(node)
            addr_to_idx[addr] = idx
            idx += 1
            node = node.next
        node = head
        while node != None:
            rand_idx = None
            if node.random:
                rand_idx = addr_to_idx[id(node.random)]
            rand_idxs.append(rand_idx)
            node = node.next

        arr = list(zip(vals, rand_idxs))
        return from_array(arr)


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            [[7,None],[13,0],[11,4],[10,2],[1,0]],
            [[7,None],[13,0],[11,4],[10,2],[1,0]],
        ),
    ]
    for (tuples, solution) in tests:
        ll = from_array(tuples)
        result = sol.copyRandomList(ll)
        print(f"ll={ll}")
        print(f"result={result}")


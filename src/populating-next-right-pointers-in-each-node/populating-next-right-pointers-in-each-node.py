# https://leetcode.com/problems/populating-next-right-pointers-in-each-node

from collections import deque

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        s = (f"Node {{ val: {self.val}, "
                f"left={'Some' if self.left else 'None'}, "
                f"right={'Some' if self.right else 'None'} "
                f"next={'Some' if self.next else 'None'} "
                "}}"
            )
        return s

    def __str__(self):
        return self.__repr__()

    def print_tree(self, indent=0):
        ind = "  " * indent
        print(f"{ind}{self}")
        if self.left: self.left.print_tree(indent=indent+1)
        if self.right: self.right.print_tree(indent=indent+1)

    @staticmethod
    def from_array(arr, index=0):
        if index >= len(arr) or arr[index] == None:
            return None
        root = Node(arr[index])
        root.left = Node.from_array(arr, 2 * index + 1)
        root.right = Node.from_array(arr, 2 * index + 2)
        return root

class Solution(object):
    def connect(self, root):
        q1 = deque([])   # queued items at the current depth level
        q2 = deque([])   # queued items at the next depth level 
        if root:
            q2.append(root)
        while len(q2) > 0 or len(q1) > 0:
            while len(q2) > 0:
                q1.append(q2.popleft())
            prev = None
            while len(q1) > 0:
                node = q1.popleft()
                if prev:
                    prev.next = node
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
                prev = node
        return root

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1,2,3,4,5,6,7]]),
    ]
    for (nums,) in tests:
        print("-------------------------")
        print("before")
        root = Node.from_array(nums)
        root.print_tree()
        print("-------------------------")
        print("after")
        sol.connect(root)
        root.print_tree()

from typing import Callable, Optional
from enum import Enum

'''
removal notes:
    1. When node is leaf, simply delete node
    2. When node has one child, replace node with child
    3. when node has 2 children, replace node with inorder succesor
'''

'''
inorder successor:
- for a given input node, the in order successor is the next node inorder
  traversal of the tree (true for all binary trees)
- in a binary search tree, the inorder succesor is also the smallest key
  greater than that of an input node
'''

'''
                9
             /     \
            /       \
           /         \
        4             13
      /  \           /    \
    3      6       11      15
  /  \   /  \    /   \    /   \
1    2  5    7   10  12  14    16
'''

class BSTException(Exception):
    pass

class BSTVisitOrderEnum(Enum):
    preorder = 0
    inorder = 1
    postorder = 3

class BSTVisitResponse(object):
    # def __init__(self, do_left: bool = True, do_right: bool = True, stop: bool = False):
    def __init__(self, stop: bool = False):
        # self.do_left: bool = do_left
        # self.do_right: bool = do_right
        self.stop: bool = stop 










class BSTNode(object):
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None

    def __str__(self) -> str:
        return f"BSTNode {{ val: `{self.val}` }}"

    def __repr__(self) -> str:
        return self.__str__()

    # *********************************
    # *** Static Utility Methods ******
    # *********************************

    @staticmethod
    def min_value(node):
        current = node
        while node.left != None:
            current = node.left
        return current.val


    @staticmethod
    def max_value(node):
        current = node
        while node.right != None:
            current = node.right
        return current.val





class BST(object):
    def __init__(self, val: int):
        self.root = BSTNode(val)

    def add(self, val: int):
        """Add `val` to the tree as a new node.
        """
        self._add(self.root, val)

    def _add(self, node: BSTNode, val):
        """Private traversal logic for public `add` method
        """
        if val < node.val:
            if node.left == None:
                node.left = BSTNode(val)
            else:
                self._add(node.left, val)
        elif val > node.val:
            if node.right == None:
                node.right = BSTNode(val)
            else:
                self._add(node.right, val)
        else:
            # val is equal to node.val, i.e this value already exists in BST
            return

    def has(self, val: int):
        """Indicate if `val` exists in the BST.
        """
        return self._has(self.root, val)

    def _has(self, node: BSTNode, val: int):
        """Private traversal logic for public `has` method
        """
        if val < node.val:
            if node.left == None:
                return False
            return self._has(node.left, val)
        elif val > node.val:
            if node.right == None:
                return False
            return self._has(node.right, val)
        else:
            # implies val == node.val
            return True

    def remove(self, val: int):
        pass

    def _remove(self, node: BSTNode, parent: BSTNode, val: int):
        pass


    def inorder_successor(self, node):
        pass



if __name__ == "__main__":
    bst = BST(1)
    # bst.root.right = BSTNode(2)
    # bst.root.left = BSTNode(0)
    bst.add(0)
    bst.add(2)
    bst.add(0)
    bst.add(-1)
    print(f"bst.has(1) = `{bst.has(1)}`")
    print(f"bst.has(2) = `{bst.has(2)}`")
    print(f"bst.has(100) = `{bst.has(100)}`")

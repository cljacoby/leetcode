from typing import Callable, Optional
from enum import Enum

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


class BSTNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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
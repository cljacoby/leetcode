import sys
from typing import Callable, Optional
from enum import Enum

"""
                9
             /     \
            /       \
           /         \
        4             13
      /  \           /    \
    3      6       11      15
  /  \   /  \    /   \    /   \
1    2  5    7  10    12  14    16
"""


class BSTError(Exception):
    pass


# ******************************************************************************
# ******************************************************************************
# ******************************************************************************


def _minimum(node):
    while node.left != None:
        node = node.left
    return node


def _maximum(node):
    while node.right != None:
        node = node.right
    return node


def _walk_inorder(node):
    if node != None:
        yield from _walk_inorder(node.left)
        yield node
        yield from _walk_inorder(node.right)


def _walk_preorder(node):
    if node != None:
        yield node
        yield from _walk_preorder(node.left)
        yield from _walk_preorder(node.right)


def _walk_postorder(node):
    if node != None:
        yield from _walk_postorder(node.left)
        yield from _walk_postorder(node.right)
        yield node


def _search_recr(node, value):
    if node == None or node.key == value:
        return node
    if value < node.key:
        return _search_recr(node.left, value)
    return _search_recr(node.right, value)


def _search_iter(node, value):
    while node != None and node.key != value:
        if value < node.key:
            node = node.left
        else:
            node = node.right
    return node


def _successor(node):
    if node == None:
        return None
    if node.right != None:
        return _minimum(node.right)
    ancestor = node.parent
    while ancestor != None and node == ancestor.right:
        node = ancestor
        ancestor = node.parent
    return ancestor


def _predecessor(node):
    if node == None:
        return None
    if node.left != None:
        return _maximum(node.left)
    ancestor = node.parent
    while ancestor != None and node == ancestor.left:
        node = ancestor
        ancestor = node.parent
    return ancestor


# NOTE: This function does not set the `depth` property. Use the actual `BST`
# class for that functionality.
def _insert(root, node):
    parent = None
    child = root
    while child != None:
        parent = child
        if node.key < child.key:
            child = child.left
        else:
            child = child.right
    node.parent = parent
    if parent == None:
        # TODO: What to do here? The `root` argument isn't reference based,
        # so can't actually update the root value.
        root = node
    elif node.key < parent.key:
        parent.left = node
    else:
        parent.right = node


# NOTE: Accepts `None` in `new` argument
def transplant(tree, old, new):
    if old.parent == None:
        tree.root = new
    elif old == old.parent.left:
        old.parent.left = new
    else:
        old.parent.right = new
    if new != None:
        new.parent = old.parent


def delete(tree, node):
    if node.left == None:
        transplant(tree, node, node.right)
    elif node.right == None:
        transplant(tree, node, node.left)
    else:
        min_node = node.right
        if min_node != node:
            transplant(tree, min_node, min_node.right)
            min_node.right = node.right
            min_node.right.parent = min_node
        transplant(tree, node, min_node)
        min_node.left = node.left
        min_node.left.parent = min_node


# ******************************************************************************
# ******************************************************************************
# ******************************************************************************


# TODO: Add `delete` method, and make sure to set `self.root` to `None` on last delete.
class BST(object):
    """
    : Binary Search Tree
    : --------------------------------------------------------------------------
    :
    """

    def __init__(self, value=None):
        self.root = None
        if value != None:
            self.root = BSTNode(value, depth=0)

    def is_empty(self):
        return self.root == None

    # TODO: Make this a cached property
    def max_depth(self):
        max_depth = self.root.depth
        for node in self.walk():
            if node.depth > max_depth:
                max_depth = node.depth
        return max_depth

    def insert(self, node):
        # Use `parent` and `child` to iteratively walk down tree and locate where
        # `node` will be inserted.
        parent = None
        child = self.root
        while child != None:
            parent = child
            if node.key < child.key:
                child = child.left
            else:
                child = child.right
        # Set `node`'s reference to it's parent. Also set the relevant `left` or
        # `right` property of the parent to new child node. Also check of parent
        # is `None`, indicating the loop was not entered and the tree is empty
        node.parent = parent
        if parent == None:
            self.root = node
            self.root.depth = 0
        else:
            if node.key < parent.key:
                parent.left = node
            else:
                parent.right = node
            node.depth = parent.depth + 1

    def walk(self):
        yield from self.root.walk_inorder()
    """
    Notes:
    * Is `depth` property 0 or 1 based index
    * Factoring in number size with the padding
    * Mix recursion and while loop to iterate on nodes at shared heigh
    """

    def print_tree(self):
        #self._print_tree(self.root, self.max_depth(), True) 
        nodes = [self.root]
        depth = 0
        max_depth = self.max_depth()
        self.__print_tree(nodes, depth, max_depth)
        
    def __print_tree(self, nodes, depth, max_depth):
        pad = " "
        next_nodes = []
        for node in nodes:
            if node != None:
                next_nodes.append(node.left)
                next_nodes.append(node.right)
            else:
                next_nodes.append(None)
                next_nodes.append(None)
        for node in nodes:
            height = max_depth - node.depth
            index = int(pow(2, height))
            next_index = int(pow(2, height - 1))
            first = False
            for in_pad_count, out_pad_count in enumerate(reversed(range(next_index, index + 1))):
                out_padding = "".join([pad] * out_pad_count)
                in_padding = "".join([pad] * (in_pad_count * 2 - 1))
                """
                print("************************")
                print(f"index = {index}")
                print(f"next_index = {next_index}")
                print(f"in_pad_count = {in_pad_count}")
                print(f"out_pad_count = {out_pad_count}")
                """
                if first:
                    line = out_padding + str(node.key) + out_padding 
                else:
                    line = out_padding + "/" + in_padding + "\\" + out_padding 
                sys.stdout.write(line)
                first = False


    def __print_tree(self):
        
        pad = " "
        max_depth = self.max_depth()
        queue = [self.root]
        
        while len(queue) > 0:
            node = queue.pop(0)
            height = max_depth - node.depth
            index = int(pow(2, height))
            next_index = int(pow(2, height - 1))


    def _print_tree(self, node, max_depth, add_newline):
        if node == None:
            return

        pad = " "
        height = max_depth - node.depth
        index = int(pow(2, height))
        next_index = int(pow(2, height - 1))
        first = True
        
        newline_slot = ""
        if add_newline:
            newline_slot = "\n"

        # for i in range(next_index, index):
        for in_pad_count, out_pad_count in enumerate(reversed(range(next_index, index + 1))):
            out_padding = "".join([pad] * out_pad_count)
            in_padding = "".join([pad] * (in_pad_count * 2 - 1))
            
            """
            print("************************")
            print(f"index = {index}")
            print(f"next_index = {next_index}")
            print(f"in_pad_count = {in_pad_count}")
            print(f"out_pad_count = {out_pad_count}")
            """

            if first:
                line = out_padding + str(node.key) + out_padding + newline_slot
            else:
                line = out_padding + "/" + in_padding + "\\" + out_padding + newline_slot
            sys.stdout.write(line)
            first = False

        self._print_tree(node.left, max_depth, False)
        right_newline = (add_newline and True)
        self._print_tree(node.right, max_depth, right_newline)


class BSTNode(object):
    """
    : Binary Search Tree Node:
    : --------------------------------------------------------------------------
    :
    : NOTE on Duplicates:
    : Duplicates are allowed (for now). This means the binary search theorem used
    : in implementation is as follows:
    : The key in each node must be GREATER than any key stored in the left subtree,
    : and the key must be LESS THAN OR EQUAL to any key stored in the right subtree.
    """

    def __init__(self, key, depth=None):
        self.key = key
        self.left = None
        self.right = None
        # TODO: Maybe seperate classes into `Node` and `BinarySearchTree` node.
        self.parent = None
        self.depth = depth

    def __str__(self) -> str:
        return f"BSTNode {{ val: `{self.key}`, depth: `{self.depth}` }}"

    def __repr__(self) -> str:
        return self.__str__()

    def minimum(self):
        node = self
        while node.left != None:
            node = node.left
        return node

    def maximum(self):
        node = self
        while node.right != None:
            node = node.right
        return node

    def succesor(self):
        """
        : Return the successor node. If all keys are distinct, then the succesor
        : of a node `x` is the node with the smallest key greater than `x.key`. If
        : node `x` has a right subtree, the successor will be the minimum node
        : in the right subtree of `x`. If the right subtree of `x` is empty, then
        : the succesor will be the lowest ancestor of `x` whose left child is also
        : an ancestor of `x`.
        """
        if self.right != None:
            return self.right.minimum()
        node = self
        ancestor = self.parent
        while ancestor != None and node == ancestor.right:
            node = ancestor
            ancestor = node.parent
        return ancestor

    def predecessor(self):
        if self.left != None:
            return self.left.maximum()
        node = self
        ancestor = self.parent
        while ancestor != None and node == ancestor.left:
            node = ancestor
            ancestor = node.parent
        return ancestor

    def search(self, value, method="iter"):
        if method == "iter":
            return _search_iter(self, value)
        elif method == "recr":
            return _search_recr(self, value)
        else:
            methods = {"iter", "test"}
            raise BSTError(
                f"Unaccepted `method` value. Accepted values are {str(methods)}."
            )

    def has(self, value):
        return self.search(value) != None

    def walk_inorder(self):
        yield from _walk_inorder(self)

    def walk_preorder(self):
        yield from _walk_preorder(self)

    def walk_postorder(self):
        yield from _walk_postorder(self)

    # TODO: not finished, doesn't print laeves
    def print_leaves(self):
        
        height = 1
        add_newline = True

        pad = " "
        # height = max_depth - node.depth
        index = int(pow(2, height))
        next_index = int(pow(2, height - 1))
        first = True
        
        newline_slot = ""
        if add_newline:
            newline_slot = "\n"

        # for i in range(next_index, index):
        for in_pad_count, out_pad_count in enumerate(reversed(range(next_index, index + 1))):
            out_padding = "".join([pad] * out_pad_count)
            in_padding = "".join([pad] * (in_pad_count * 2 - 1))
            
            """
            print("************************")
            print(f"index = {index}")
            print(f"next_index = {next_index}")
            print(f"in_pad_count = {in_pad_count}")
            print(f"out_pad_count = {out_pad_count}")
            """

            if first:
                line = out_padding + str(node.key) + out_padding + newline_slot
            else:
                line = out_padding + "/" + in_padding + "\\" + out_padding + newline_slot
            sys.stdout.write(line)
            first = False


if __name__ == "__main__":
    root = BSTNode(5)
    root.left = BSTNode(3)
    root.right = BSTNode(7)
    root.left.left = BSTNode(1)
    root.left.right = BSTNode(4)
    root.right.left = BSTNode(6)
    root.right.right = BSTNode(8)

    print("## Inorder walk test")
    for node in root.walk_inorder():
        print(node)

    print("## Preorder walk test")
    for node in root.walk_preorder():
        print(node)

    print("## Postorder walk test")
    for node in root.walk_postorder():
        print(node)

    print("## Test search_iter and search_recr, positive tests")
    print(_search_recr(root, 5))
    print(_search_iter(root, 5))

    print("## Test search_iter and search_recr, negative tests")
    print(_search_iter(root, 100))
    print(_search_recr(root, 100))
    print(_search_iter(root, -5))
    print(_search_recr(root, -5))

    print("## Test has")
    print(root.has(5))
    print(root.has(100))

    print("## Test minimum and maximum")
    print(_minimum(root))
    print(_maximum(root))

    print("## Test successor and predecessor")
    print(root.right)
    print(_successor(root.right))
    print(_predecessor(root.right))

    print("## Using `BST` class here and below.")
    bst = BST()
    bst.insert(BSTNode(5))
    bst.insert(BSTNode(1))
    bst.insert(BSTNode(-4))
    bst.insert(BSTNode(4))
    bst.insert(BSTNode(1))
    bst.insert(BSTNode(0))
    bst.insert(BSTNode(100))
    bst.insert(BSTNode(24))
    bst.insert(BSTNode(45))
    bst.insert(BSTNode(86))    
    for node in bst.walk():
        print(node)

    # bst.print_tree()
    bst.root.print_leaves()

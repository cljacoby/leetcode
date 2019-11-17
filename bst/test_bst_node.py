import unittest
from types import SimpleNamespace
import random
from bst import BSTNode, _insert


class TestBSTNode(unittest.TestCase):
    def setUp(self):
        pass

    def random_tree(self, size=20, min_val=-100, max_val=100):
        """
        : Generate a Binary Search Tree of random integers. This tree is composed
        : of `BinarySearchTree` nodes strung together, rather than an actual instance
        : `BinarySearchTree`. Used for testing `BinarySearchTreeNode`'s methods.
        """
        values = [random.randint(min_val, max_val) for i in range(size)]
        minimum = min(values)
        maximum = max(values)
        index = random.randint(0, size - 1)
        # This creates a duplicate of whichever value lies at `index`.
        root = BSTNode(values[index])
        for val in values:
            _insert(root, BSTNode(val))
        obj = SimpleNamespace(
            root=root, minimum=minimum, maximum=maximum, values=values
        )
        return obj

    def consistent_tree(self):
        """
        : Generate a Binary Search Tree of consistent integers. This tree is composed
        : of `BinarySearchTree` nodes strung together, rather than an actual instance
        : `BinarySearchTree`. Used for testing `BinarySearchTreeNode`'s methods.
        """
        root_val = 6
        values = [-10, -6, 43, 65, 12, 43, 90, 3, 71, 3, -234, 94, 5]
        minimum = min(values)
        maximum = max(values)
        root = BSTNode(root_val)
        for val in values:
            _insert(root, BSTNode(val))
        # Append `root_val` to `values` for full list of tree's values.
        values.append(root_val)
        obj = SimpleNamespace(
            root=root, minimum=minimum, maximum=maximum, values=values
        )
        return obj

    def test_bst_node_init(self):
        """
        : Test the __init__ method of the BSTNode.
        """
        bst_node = BSTNode(5)
        self.assertEqual(bst_node.key, 5)
        self.assertEqual(bst_node.left, None)
        self.assertEqual(bst_node.right, None)
        self.assertEqual(bst_node.parent, None)

    def test_bst_node_left(self):
        """
        : Test the `left` reference works as expected.
        """
        tree_obj = self.consistent_tree()
        root = tree_obj.root
        self.assertEqual(type(root.left), BSTNode)
        self.assertEqual(root.left.key, -10)
        self.assertEqual(type(root.left.left), BSTNode)
        self.assertEqual(root.left.left.key, -234)

    def test_bst_node_right(self):
        """
        : Test the `right` reference works as expected.
        """
        tree_obj = self.consistent_tree()
        root = tree_obj.root
        self.assertEqual(type(root.right), BSTNode)
        self.assertEqual(root.right.key, 43)
        self.assertEqual(type(root.right.right), BSTNode)
        self.assertEqual(root.right.right.key, 65)

    def test_bst_node_minimum(self):
        """
        : Test the `minimum` method of the BSTNode using a consistently generated tree.
        """
        tree_obj = self.consistent_tree()
        root = tree_obj.root
        self.assertEqual(root.minimum().key, tree_obj.minimum)

    def test_bst_node_minimum_random(self):
        """
        : Test the `minimum` method of the BSTNode using a randomly generated tree.
        """
        tree_obj = self.random_tree()
        root = tree_obj.root
        self.assertEqual(root.minimum().key, tree_obj.minimum)

    def test_bst_node_maximum(self):
        """
        : Test the `maximum` method of the BSTNode using a consistently generated tree.
        """
        tree_obj = self.consistent_tree()
        root = tree_obj.root
        self.assertEqual(root.maximum().key, tree_obj.maximum)

    def test_bst_node_maximum_random(self):
        """
        : Test the `maximum` method of the BSTNode using a randomly generated tree.
        """
        tree_obj = self.random_tree()
        root = tree_obj.root
        self.assertEqual(root.maximum().key, tree_obj.maximum)

    def test_bst_node_has(self):
        """
        : Test the `has` method of the BSTNode using a randomly generated tree.
        """
        tree_obj = self.random_tree(min_val=-100, max_val=100)
        root, values = tree_obj.root, tree_obj.values
        for val in tree_obj.values:
            self.assertTrue(root.has(val))
        self.assertFalse(root.has(101))
        self.assertFalse(root.has(-101))

    def test_bst_node_search(self):
        """
        : Test the `search` method of the BSTNode using a randomly generated tree.
        """
        tree_obj = self.random_tree(min_val=-100, max_val=100)
        root, values = tree_obj.root, tree_obj.values
        for val in tree_obj.values:
            node = root.search(val) 
            self.assertEqual(type(node), BSTNode)
            self.assertEqual(node.key, val)
        self.assertFalse(root.search(-101), None)
        self.assertFalse(root.search(101), None)

    def test_bst_node_succesor(self):
        tree_obj = self.random_tree()
        root, values = tree_obj.root, tree_obj.values
        print(sorted(values))
        for node in root.walk_inorder():
            print(node, node.succesor())

    def tearDown(self):
        pass

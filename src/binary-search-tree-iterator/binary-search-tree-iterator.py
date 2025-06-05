# https://leetcode.com/problems/binary-search-tree-iterator

from TreeNode import TreeNode

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.post = []
        self.dive(root)

    def dive(self, root):
        while root != None:
            self.post.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        if len(self.post) == 0:
            raise Exception("called next with no more nodes")
        node = self.post.pop()
        self.dive(node.right)
        return node.val


    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.post) > 0

    def __repr__(self):
        s = f"BSTIterator {{ post={self.post} }}"
        return s

if __name__ == "__main__":
    tests = [
        (
            [7, 3, 15, None, None, 9, 20],
            ["next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"],
            [3,      7,       True,     9,      True,       15,    True,      20,      False],
        ),
        (
            [1, None, 2],
            ["hasNext","next","hasNext","next","hasNext"],
            [True, 1, True, 2, False]
        )
    ]
    for (nums, methods, rets) in tests:
        tree = TreeNode.from_array(nums)
        tree.print_tree()
        bst = BSTIterator(tree)
        for method, ret in zip(methods, rets):
            f = getattr(bst, method)
            out = f()
            print(f"out={out}, ret={ret}, method={method}, bst={bst}")
            assert out == ret, \
                f"out {out} != ret {ret}, method = {method}, bst={bst}"
    print("✅ All tests passed")


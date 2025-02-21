# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree

from TreeNode import TreeNode

class FindElements(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.cache = set()
        self.recover(root, 0)

    def recover(self, node, val):
        if node == None:
            return
        self.cache.add(val)
        self.recover(node.left, 2 * val + 1)
        self.recover(node.right, 2 * val + 2)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.cache

if __name__ == "__main__":
    cases = [
        (
            [-1,None,-1],
            [
                (1, False),
                (2, True),
            ]
        ),
        (
            [-1,-1,-1,-1,-1],
            [
                (1, True),
                (2, True),
                (5, False),
            ]
        ),
        (
            [-1,None,-1,-1,None,-1],
            [
                (2, True),
                (3, False),
                (4, False),
                (5, True),
            ]
        ),
    ]
    for (arr, tests) in cases:
        tree = TreeNode.from_array(arr)
        find = FindElements(tree)
        for (x, solution) in tests:
            res = find.find(x)
            assert res == solution, \
                f"res {res} != solution {solution}\nx = {x}, tree = {tree}, find = {find}"
    print("✅ All tests passed")


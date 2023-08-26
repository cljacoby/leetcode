# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

from TreeNode import TreeNode


class Solution(object):
    def path_to_node(self, root, x, path):
        if root == None:
            return False
        path.append(root)
        if (
            root.val == x
            or self.path_to_node(root.left, x, path)
            or self.path_to_node(root.right, x, path)
        ):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_p = list()
        path_q = list()
        assert self.path_to_node(root, p.val, path_p), \
                f"Path to node p={p.val} not found"
        assert self.path_to_node(root, q.val, path_q), \
                f"Path to node q={q.val} not found"
        last = None
        for i, (a, b) in enumerate(zip(path_p, path_q)):
            if a.val != b.val:
                break
            last = a
        return last


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 7, 4, 2),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
    ]
    for (arr, p, q, solution) in tests:
        tree = TreeNode.from_array(arr)
        p = TreeNode(p)
        q = TreeNode(q)
        node = sol.lowestCommonAncestor(tree, p, q)
        assert node.val == solution, \
                f"node.val {node.val} != solution {solution}"
    print("✅ All tests passed")

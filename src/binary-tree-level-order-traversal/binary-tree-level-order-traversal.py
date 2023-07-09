# https://leetcode.com/problems/binary-tree-level-order-traversal

from TreeNode import TreeNode
from collections import deque, defaultdict


# More ergonomic solution using defaultdict. Also a little slower, and
# uses more memory. Needs to convert the defaultdict into the output 2d
# list at the end.
class _Solution(object):
    def def_dict_to_list(self, d):
        arr = [[] for i in d]
        for (idx, vals) in d.items():
            arr[idx].extend(vals)
        return arr

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = deque([(0, root)])
        levels = defaultdict(list)
        while len(q) > 0:
            (lvl, node) = q.popleft()
            levels[lvl].append(node.val)
            if node.left:
                q.append((lvl + 1, node.left))
            if node.right:
                q.append((lvl + 1, node.right))
        return self.def_dict_to_list(levels)


# Faster and lower memory use, but slightly less easy to interpret.
# Directly build the `levels` return value as a 2d list. As levels are
# going up, need to check if the current list size is long enough, and
# extend if needed.
class Solution(object):
    def extend(self, levels, lvl):
        levels.extend([[] for i in range(len(levels) - lvl + 1)])

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = deque([(0, root)])
        levels = [[]]
        while len(q) > 0:
            (lvl, node) = q.popleft()
            if lvl >= len(levels):
                self.extend(levels, lvl)
            levels[lvl].append(node.val)
            if node.left:
                q.append((lvl + 1, node.left))
            if node.right:
                q.append((lvl + 1, node.right))
        return levels


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
    ]
    for (nums, solution) in tests:
        tree = TreeNode.from_array(nums)
        result = sol.levelOrder(tree)
        assert result == solution, \
            f"result {result} != solution {solution}"
    print("✅ All tests passed")

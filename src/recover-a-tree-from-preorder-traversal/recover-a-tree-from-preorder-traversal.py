# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal

from TreeNode import TreeNode
from collections import deque
import re

class Solution(object):
    def parse(self, s):
        nodes = deque([])
        pattern = r"(-{0,})(\d+)"
        toks = re.findall(pattern, s)
        for dashes, digit in toks:
            nodes.append((len(dashes), int(digit)))
        return nodes

    def recoverFromPreorder(self, s):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        q = self.parse(s)
        if len(q) == 0:
            return None
        (depth, val) = q.popleft()
        root = TreeNode(val)
        root.depth = depth
        self.step(q, root)
        return root

    def step(self, q, root):
        # left
        if (len(q) == 0 or q[0][0] != root.depth + 1):
            return
        (depth, val) = q.popleft()
        node = TreeNode(val)
        node.depth = depth
        root.left = node
        self.step(q, root.left)

        # right
        if (len(q) == 0 or q[0][0] != root.depth + 1):
            return
        (depth, val) = q.popleft()
        node = TreeNode(val)
        node.depth = depth
        root.right = node
        self.step(q, root.right)

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            "1-2--3--4-5--6--7",
            [1,2,5,3,4,6,7],
        ),
        (
            "1-2--3---4-5--6---7",
            [1,2,5,3,None,6,None,4,None,7],
        ),
        (
            "1-401--349---90--88",
            [1,401,None,349,88,90],
        ),
    ]
    for (s, arr) in tests:
        print("*********************************************")

        tree = sol.recoverFromPreorder(s)
        print("tree:")
        tree.print_tree()

        solution = TreeNode.from_array(arr)
        print("solution:")
        solution.print_tree()


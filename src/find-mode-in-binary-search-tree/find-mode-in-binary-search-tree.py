# https://leetcode.com/problems/find-mode-in-binary-search-tree

from TreeNode import TreeNode
from collections import defaultdict

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.freq = defaultdict(int)
        self.mode = -1
        self.step(root)
        modes = []
        for (x, count) in self.freq.items():
            if count == self.mode:
                modes.append(x)
        return modes

    def step(self, node):
        if node == None:
            return
        self.freq[node.val] += 1
        self.mode = max(self.mode, self.freq[node.val])
        self.step(node.left)
        self.step(node.right)
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1,None,2,None,None,2], [2]),
        ([0], [0])
    ]
    for (arr, solution) in tests:
        tree = TreeNode.from_array(arr)
        result = sol.findMode(tree)
        assert set(result) == set(solution), \
            f"wrong answer, solution={solution}, result={result}"
    print("✅ All tests passed")


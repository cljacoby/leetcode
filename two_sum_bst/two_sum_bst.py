class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def add_left(self, node: TreeNode):
    def add_left(self, node):
        # self.left = TreeNode(val)
        self.left = node
        return self

    # def add_right(self, node: TreeNode):
    def add_right(self, node):
        # self.right = TreeNode(val)
        self.right = node
        return self

    def print_tree(self):
        pass

    def bfs(self):
        que = []
        que.appendself):
        while len(que) > 0:
            node = que.pop()

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        self.nodes_into_dict(root, k, d)
        print(s)

    def nodes_into_set(self, root: TreeNode, s: set) -> bool:
        s.add(root.val)
        if root.left:
            nodes_into_set(root.left, s)
        if root.right:
            nodes_into_set(root.right, s)


if __name__ == "__main__":
    solution = Solution()
    tests = []
    root = (
        TreeNode(0)
            .add_left(TreeNode(1)
                .add_left(2)
                .add_right(3)
            )
            .add_right(TreeNode(4))
    )
    for root, target in tests:
        solution.findTarget(root, target)

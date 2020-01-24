# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def set_left(self, branch: TreeNode):
    def set_left(self, branch):
        self.left = branch 
        return self

    # def set_right(self, branch: TreeNode):
    def set_right(self, branch):
        self.right = branch 
        return self

    def __repr__(self):
        return f"TreeNode {{ val: {self.val} }}"

    def __str__(self):
        return self.__repr__()

    def print(self, indents=0, char="\t"):
        indent = "".join([char for i in range(indents)])
        print(f"{indent}{str(self)}")
        if self.left:
            self.left.print(indents + 1)
        if self.right:
            self.right.print(indents + 1)


# print(f"Node: {str(root)}, gparent: {str(gparent)}, return: {sum}")
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self._sumEvenGrandparent(root, None, None)

    def _sumEvenGrandparent(self, root, parent, gparent):
        sum_left, sum_right = 0, 0
        if root.left:
            sum_left = self._sumEvenGrandparent(root.left, root, parent)
        if root.right:
            sum_right = self._sumEvenGrandparent(root.right, root, parent)
        sum = sum_left + sum_right
        if gparent != None and gparent.val % 2 == 0:
            sum += root.val
        return sum

if __name__ == "__main__":
    TN = TreeNode
    root = (TN(6)
        .set_left(TN(7)
            .set_left(TN(2)
                .set_left(TN(9))
            )
            .set_right(TN(7)
                .set_left(TN(1))
                .set_right(TN(4))
            )
        )
        .set_right(TN(8)
            .set_left(TN(1))
            .set_right(TN(3)
                .set_right(TN(5))    
            ) 
        )
    )
    root.print()
    sol = Solution()
    print(sol.sumEvenGrandparent(root))

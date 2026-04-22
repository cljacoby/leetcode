# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        s = (f"TreeNode {{ val: {self.val}, "
                f"left={'Some' if self.left else 'None'}, "
                f"right={'Some' if self.right else 'None'} "
                "}}"
            )
        return s

    def __str__(self):
        return self.__repr__()

    def print_tree(self, indent=0):
        ind = "  " * indent
        print(f"{ind}{self}")
        if self.left: self.left.print_tree(indent=indent+1)
        if self.right: self.right.print_tree(indent=indent+1)

    @staticmethod
    def from_array(arr, index=0):
        if index >= len(arr) or arr[index] == None:
            return None
        root = TreeNode(arr[index])
        root.left = TreeNode.from_array(arr, 2 * index + 1)
        root.right = TreeNode.from_array(arr, 2 * index + 2)
        return root



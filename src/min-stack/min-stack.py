# https://leetcode.com/problems/min-stack


class MinStack(object):
    def __init__(self):
        self.stack = list()

    def __repr__(self):
        return f"MinStack {{ stack: {self.stack} }}"
    
    def __str__(self):
        return self.__repr__()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.getMin())))

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            raise Exception("Pop from empty stack")
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            raise Exception("Top from empty stack")
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            raise Exception("Min from empty stack")
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    tests = [
        ("push",    -2,     None),
        ("push",    0,      None),
        ("push",    -3,     None),
        ("getMin",  None,   -3),
        ("pop",     None,   None),
        ("top",     None,   0),
        ("getMin",  None,   -2),
    ]
    min_stack = MinStack()
    for (func, arg, out) in tests:
        method = getattr(min_stack, func)
        ret = method(arg) if arg != None else method()
        if out != None:
            assert out == ret, \
                f"method {method} with arg {arg} gave ret {ret} not equal to out {out}"
    print("✅ All tests passed")

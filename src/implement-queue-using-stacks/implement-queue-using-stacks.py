# https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue(object):

    def __init__(self):
        self.input = list()
        self.output = list()
    
    def _shift(self):
        """
        When output is empty, and input is not,
        move all elements from input to output,
        reversing the ordering in the process.
        """
        if len(self.output) == 0:
            while len(self.input) > 0:
                x = self.input.pop()
                self.output.append(x)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self._shift()
        assert len(self.output) > 0, "Popped from empty queue"
        return self.output.pop()

    def peek(self):
        """
        :rtype: int
        """
        self._shift()
        assert len(self.output) > 0, "Peeked from empty queue"
        return self.output[-1]

    def empty(self):
        """
        :rtype: bool
        """
        self._shift()
        return len(self.output) == 0

if __name__ == "__main__":
    tests = [
        ("push",        1,      None),
        ("push",        2,      None),
        ("peek",        None,   1),
        ("pop",         None,   1),
        ("empty",       None,   False),
    ]
    queue = MyQueue()
    for (method, arg, solution) in tests:
        if arg:
            result = getattr(queue, method)(arg)
        else:
            result = getattr(queue, method)() 
        assert result == solution, \
            f"call to {method} gave result {result} != solution {solution}"
    print("✅ All tests passed")


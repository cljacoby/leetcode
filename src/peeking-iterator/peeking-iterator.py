# https://leetcode.com/problems/peeking-iterator

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self._next()
    
    def _next(self):
        # Leetcode question formualtion is stupid.
        # try:
        #     self.ondeck = next(self.iterator)
        # except StopIteration:
        #     self.ondeck = None
        if self.iterator.hasNext():
            self.ondeck = self.iterator.next()
        else:
            self.ondeck = None
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.ondeck
        

    def next(self):
        """
        :rtype: int
        """
        ondeck = self.ondeck
        self._next()
        return ondeck
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ondeck != None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

if __name__ == "__main__":
    tests = [
        ["next",    "peek", "next", "next", "hasNext"],
        [[],        [],     [],     [],     [],      ],
        [1,         2,      2,      3,      False]
    ]
    peeking_iter = PeekingIterator(iter([1, 2, 3]))
    for (method, args, ret) in zip(tests[0], tests[1], tests[2]):
        f = getattr(peeking_iter, method)
        out = f(*args)
        print(f"out={out}, ret={ret}, method={method}, args={args}, f={f}")
        assert out == ret, \
            f"out={out} != ret={ret}, method={method}, args={args}"
    print("✅ All tests passed")


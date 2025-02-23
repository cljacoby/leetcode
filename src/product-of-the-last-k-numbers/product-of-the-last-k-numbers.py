# https://leetcode.com/problems/product-of-the-last-k-numbers

class ProductOfNumbers(object):
    def __init__(self):
        self.arr = []
        self.count = 0

    def add(self, num):
        """
        :type num: int
        :rype: None
        """
        self.count += 1
        if num == 0:
            self.arr = []
        elif len(self.arr) == 0:
            self.arr.append(num)
        else:
            self.arr.append(num * self.arr[-1])

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        assert k < self.count, \
            f"called getProduct with k={k}, but count was only {self.count}"
        if k < len(self.arr):
            return self.arr[-1] // self.arr[-(k+1)]
        elif len(self.arr) == k:
            return self.arr[-1]
        else:
            return 0

if __name__ == "__main__":
    prod = ProductOfNumbers()
    cmds = [
        ["add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"],
        [[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]],
        [None,None,None,None,None,20,40,0,None,32],
    ]
    for (method, args, solution) in zip(*cmds):
        print(f"method={method}, args={args}, solution={solution}")
        f = getattr(prod, method)
        ret = f(*args)
        assert ret == solution, \
            f"ret {ret} != solution {solution}, method={method}, args={args}"
    print("✅ All tests passed")


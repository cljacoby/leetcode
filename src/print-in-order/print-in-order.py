# https://leetcode.com/problems/print-in-order

from threading import Thread, Lock
import time
from random import random

class Foo(object):
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        printFirst()
        self.locks[0].release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        with self.locks[0]:
            printSecond()
            self.locks[1].release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        with self.locks[1]:
            printThird()

def print_cb(s):
    def cb():
        time.sleep(random() * 1)
        print(s)
    return cb

if __name__ == "__main__":
    foo = Foo()

    t1 = Thread(target=Foo.first, args=(foo, print_cb("first")))
    t2 = Thread(target=Foo.second, args=(foo, print_cb("second")))
    t3 = Thread(target=Foo.third, args=(foo, print_cb("third")))

    t1.start()
    t3.start()
    t2.start()

    t1.join()
    t2.join()
    t3.join()

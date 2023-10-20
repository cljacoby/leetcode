# https://leetcode.com/problems/design-browser-history

from DoubleListNode import DoubleListNode

# Implementation using doubly linked list
class BrowserHistory(object):

    def __init__(self, homepage):
        self.homepage = homepage
        node = DoubleListNode(self.homepage)
        self.curr = node

    def visit(self, url):
        node = DoubleListNode(url)
        if self.curr == None:
            self.curr = node
        else:
            self.curr.next = node
            node.prev = self.curr
            self.curr = node

    def back(self, steps):
        i = 0
        while i < steps and self.curr.prev != None:
            self.curr = self.curr.prev
            i += 1
        return self.curr.val
        

    def forward(self, steps):
        i = 0
        while i < steps and self.curr.next != None:
            self.curr = self.curr.next
            i += 1
        return self.curr.val
        
# Implementaiton using 2 lists
class BrowserHistory:
    def __str__(self):
        return f"BrowserHistory {{ hist: {self.hist}, fhist: {self.fhist} }}"

    def __repr__(self):
        return self.__str__()

    def __init__(self, homepage: str):
        self.hist = list([homepage])
        self.fhist = list()

    def visit(self, url: str) -> None:
        self.hist.append(url)
        self.fhist.clear()
        

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.hist) > 1:
            self.fhist.append(self.hist.pop())
            steps -= 1
        return self.hist[-1]
        

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.fhist) > 0:
            self.hist.append(self.fhist.pop())
            steps -= 1
        return self.hist[-1]


if __name__ == "__main__":
    hist = BrowserHistory("leetcode.com")
    ops = [
        ("visit",        "google.com",       None,              ), 
        ("visit",        "facebook.com",     None,              ), 
        ("visit",        "youtube.com",      None,              ), 
        ("back",         1,                  "facebook.com",    ), 
        ("back",         1,                  "google.com",      ), 
        ("forward",      1,                  "facebook.com",    ), 
        ("visit",        "linkedin.com",     None,              ), 
        ("forward",      2,                  "linkedin.com",    ), 
        ("back",         2,                  "google.com",      ), 
        ("back",         7,                  "leetcode.com",    ),
    ]
    for (method, arg, ret) in ops:
        func = getattr(hist, method)
        out = func(arg)
        assert ret == out, \
            f"ret {ret} != out {out}"
    print("✅ All tests passed")


class Node:
    def __init__(self, x, n):
        self.x = x
        self.next = n

class MinStack:
    # @param x, an integer
    # @return an integer
    self.min = None
    self.top = None
    def push(self, x):
        if not self.top:
            t = Node(x, None)
            self.top = t
            self.min = t
            return
        t = self.top
        while t:
            if x < t.x:
                a = Node()

    # @return nothing
    def pop(self):
        if not self.top:
            return
        t = self.min
        while t:
            if t.x == self.top.x:
                t.x = t.next.x
                t.next = t.next.next
                break
            t = t.next
        self.top = self.top.next
        return

    # @return an integer
    def top(self):
        return self.top.x

    # @return an integer
    def getMin(self):
        return self.min.x
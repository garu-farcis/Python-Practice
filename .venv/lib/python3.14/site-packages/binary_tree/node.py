class node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None

    def addValue(self, n):
        if n < self.n:
            if self.left:
                self.left.addValue(n)
            else:
                self.left = node(n)
        elif n > self.n:
            if self.right:
                self.right.addValue(n)
            else:
                self.right = node(n)

    def visit(self):
        l = []
        if self.left:
            l += self.left.visit()
        l.append(self.n)
        if self.right:
            l += self.right.visit()
        return l

    def search(self, n):
        if self.n is n:
            return True
        elif self.n < n and self.right:
            return self.right.search(n)
        elif self.left:
            return self.left.search(n)
        else:
            return False

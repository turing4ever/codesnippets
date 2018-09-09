class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.append(x)
        size = len(self.q)
        while size > 1:
            self.q.append(self.q.pop(0))
            size -= 1
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.pop(0)
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.q):
            return self.q[0]
        else:
            return None
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

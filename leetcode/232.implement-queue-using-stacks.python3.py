class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = []
        self.right = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self.right:
            self.left.append(self.right.pop())
        self.left.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.left:
            self.right.append(self.left.pop())
        return self.right.pop() if self.right else None
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.left:
            self.right.append(self.left.pop())
        return self.right[-1] if self.right else None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.left and not self.right


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

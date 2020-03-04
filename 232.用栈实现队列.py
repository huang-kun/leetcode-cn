#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = [] # 负责入队
        self.outStack = [] # 负责出队


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.outStack):
            return self.outStack.pop()
        
        while len(self.inStack):
            self.outStack.append(self.inStack.pop())
        
        return self.outStack.pop() if len(self.outStack) else None


    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.outStack):
            return self.outStack[-1]
        elif len(self.inStack):
            return self.inStack[0]
        return None


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.inStack) == 0 and len(self.outStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end


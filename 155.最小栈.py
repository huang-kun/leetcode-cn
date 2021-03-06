#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start

# 参考了用户@Krahets的题解，恍然大悟，怎么自己就没想到呢。。
# https://leetcode-cn.com/problems/min-stack/solution/min-stack-fu-zhu-stackfa-by-jin407891080/
class MinStack:

    def __init__(self):
        self.list = []
        self.mlist = []

    def push(self, x: int) -> None:
        self.list.append(x)
        if len(self.mlist) == 0:
            self.mlist.append(x)
        elif self.mlist[-1] >= x:
            self.mlist.append(x)

    def pop(self) -> None:
        x = self.list.pop()
        if self.mlist[-1] == x:
            self.mlist.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.mlist[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


# 以下是第一个版本的代码，在每次入栈时比较和保留最小值，
# 而在出栈后，只有在删除了最小值的情况下，才需要重新计算剩余元素的最小值。
# 最坏的情况下，每次入栈的数字都是越来越小，那么每次出栈的时间复杂度为O(n)
class MinStack1:
    def __init__(self):
        self.list = []
        self.min = None

    def push(self, x: int) -> None:
        self.list.append(x)
        self.min = min(self.min, x) if self.min is not None else x

    def pop(self) -> None:
        x = self.list.pop()
        if x == self.min:
            self.min = None
            for n in self.list:
                self.min = min(self.min, n) if self.min is not None else n

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min